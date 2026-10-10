let videos = [];

const CACHE_KEY = "youtube_bulk_editor_cache_v1";

function saveCache(sourceLabel) {
  try {
    const prevCache = loadCache();
    const prevLabel = prevCache && prevCache.sourceLabel;
    localStorage.setItem(
      CACHE_KEY,
      JSON.stringify({
        videos,
        fetchedAt: new Date().toISOString(),
        sourceLabel: sourceLabel || prevLabel || "全動画",
      })
    );
  } catch (e) {
    // 容量オーバー等は無視（キャッシュが使えないだけで動作には影響しない）
  }
}

function loadCache() {
  try {
    const raw = localStorage.getItem(CACHE_KEY);
    return raw ? JSON.parse(raw) : null;
  } catch (e) {
    return null;
  }
}

const statusEl = document.getElementById("status");
const loadBtn = document.getElementById("loadBtn");
const clearCacheBtn = document.getElementById("clearCacheBtn");
const sourceSelect = document.getElementById("sourceSelect");
const refreshPlaylistsBtn = document.getElementById("refreshPlaylistsBtn");
const toolbar = document.getElementById("toolbar");
const table = document.getElementById("videoTable");
const tbody = document.getElementById("videoTableBody");
const filterBox = document.getElementById("filterBox");
const filterPrivacySelect = document.getElementById("filterPrivacy");
const sortSelect = document.getElementById("sortSelect");
const selectAll = document.getElementById("selectAll");
const selectedCountEl = document.getElementById("selectedCount");
const bulkApplyBtn = document.getElementById("bulkApplyBtn");
const bulkPrivacySelect = document.getElementById("bulkPrivacy");
const saveAllBtn = document.getElementById("saveAllBtn");

const PRIVACY_LABEL = {
  public: "公開",
  unlisted: "限定公開",
  private: "非公開",
};

loadBtn.addEventListener("click", loadVideos);
clearCacheBtn.addEventListener("click", clearCache);
refreshPlaylistsBtn.addEventListener("click", loadPlaylistOptions);
filterBox.addEventListener("input", renderTable);
filterPrivacySelect.addEventListener("change", renderTable);
sortSelect.addEventListener("change", renderTable);
selectAll.addEventListener("change", () => {
  // フィルタで絞り込んだ表示中の行だけが対象（tbodyには表示中の行しか無い）
  tbody
    .querySelectorAll('input[type="checkbox"][data-id]')
    .forEach((cb) => {
      cb.checked = selectAll.checked;
    });
  updateSelectedCount();
});
bulkApplyBtn.addEventListener("click", bulkApply);
saveAllBtn.addEventListener("click", saveAllDirtyRows);

async function loadPlaylistOptions() {
  refreshPlaylistsBtn.disabled = true;
  const originalText = refreshPlaylistsBtn.textContent;
  refreshPlaylistsBtn.textContent = "取得中...";
  try {
    const res = await fetch("/api/playlists");
    const data = await res.json();
    if (!data.ok) throw new Error(data.error || "プレイリスト一覧の取得に失敗したよ");

    const currentValue = sourceSelect.value;
    sourceSelect.innerHTML = '<option value="all">全動画</option>';
    for (const p of data.playlists) {
      const opt = document.createElement("option");
      opt.value = `playlist:${p.id}`;
      opt.textContent = `📁 ${p.title}（${p.itemCount}件）`;
      sourceSelect.appendChild(opt);
    }
    // 前に選んでたものがまだ一覧にあれば復元
    if ([...sourceSelect.options].some((o) => o.value === currentValue)) {
      sourceSelect.value = currentValue;
    }
  } catch (e) {
    alert(`プレイリスト一覧の取得に失敗したよ: ${e.message}`);
  } finally {
    refreshPlaylistsBtn.disabled = false;
    refreshPlaylistsBtn.textContent = originalText;
  }
}

async function loadVideos() {
  loadBtn.disabled = true;
  statusEl.textContent = "取得中...（動画数が多いと少し時間かかるよ。APIの1日の利用上限に注意！）";
  try {
    const source = sourceSelect.value;
    const endpoint =
      source === "all" ? "/api/videos" : `/api/playlists/${source.replace("playlist:", "")}/videos`;
    const res = await fetch(endpoint);
    const data = await res.json();
    if (!data.ok) {
      throw new Error(data.error || "取得に失敗したよ");
    }
    videos = data.videos;
    const sourceLabel = source === "all" ? "全動画" : sourceSelect.selectedOptions[0].textContent;
    saveCache(sourceLabel);
    statusEl.textContent = `${sourceLabel}: ${videos.length}件の動画を取得したよ（${formatNow()}時点）`;
    toolbar.hidden = false;
    table.hidden = false;
    renderTable();
  } catch (e) {
    statusEl.textContent = `エラー: ${e.message}`;
  } finally {
    loadBtn.disabled = false;
  }
}

function clearCache() {
  if (!confirm("表示中の一覧とキャッシュを消すよ（YouTube側は何も変更されないよ）。いい？")) {
    return;
  }
  try {
    localStorage.removeItem(CACHE_KEY);
  } catch (e) {
    // ignore
  }
  videos = [];
  tbody.innerHTML = "";
  toolbar.hidden = true;
  table.hidden = true;
  statusEl.textContent = "キャッシュをクリアしたよ。「動画一覧を取得」で最新を取り直してね";
}

function formatNow() {
  return new Date().toLocaleString("ja-JP");
}

// ページを開いた時、前回取得したキャッシュがあれば自動で復元する
// （毎回APIを叩き直すとGoogle側の1日の利用上限をすぐ使い切ってしまうため）
function restoreFromCache() {
  const cache = loadCache();
  if (!cache || !cache.videos || cache.videos.length === 0) return;

  videos = cache.videos;
  const fetchedAt = new Date(cache.fetchedAt).toLocaleString("ja-JP");
  const sourceLabel = cache.sourceLabel || "全動画";
  statusEl.textContent = `前回取得したキャッシュを表示中（${sourceLabel} / 取得日時: ${fetchedAt}）。最新化するには「動画一覧を取得」を押してね`;
  toolbar.hidden = false;
  table.hidden = false;
  renderTable();
}

restoreFromCache();

function getVisibleVideos() {
  const keyword = filterBox.value.trim().toLowerCase();
  const privacyFilter = filterPrivacySelect.value;

  let list = videos.filter((v) => {
    if (keyword && !v.title.toLowerCase().includes(keyword)) return false;
    if (privacyFilter && v.privacyStatus !== privacyFilter) return false;
    return true;
  });

  const [field, direction] = sortSelect.value.split("_");
  const dir = direction === "asc" ? 1 : -1;
  list = list.slice().sort((a, b) => {
    let av = a[field];
    let bv = b[field];
    if (field === "likeCount") {
      // いいね数非公開の動画(null)は常に末尾に回す
      if (av == null && bv == null) return 0;
      if (av == null) return 1;
      if (bv == null) return -1;
    } else {
      av = (av || "").toString().toLowerCase();
      bv = (bv || "").toString().toLowerCase();
    }
    if (av < bv) return -1 * dir;
    if (av > bv) return 1 * dir;
    return 0;
  });

  return list;
}

function renderTable() {
  tbody.innerHTML = "";

  for (const v of getVisibleVideos()) {
    const tr = document.createElement("tr");
    tr.dataset.id = v.id;

    const cbTd = document.createElement("td");
    const cb = document.createElement("input");
    cb.type = "checkbox";
    cb.dataset.id = v.id;
    cb.addEventListener("change", updateSelectedCount);
    cbTd.appendChild(cb);
    tr.appendChild(cbTd);

    const thumbTd = document.createElement("td");
    if (v.thumbnail) {
      const img = document.createElement("img");
      img.className = "thumb";
      img.src = v.thumbnail;
      thumbTd.appendChild(img);
    }
    tr.appendChild(thumbTd);

    const titleTd = document.createElement("td");
    const titleInput = document.createElement("input");
    titleInput.className = "titleInput";
    titleInput.value = v.title;
    titleInput.addEventListener("input", () => tr.classList.add("dirty"));
    titleTd.appendChild(titleInput);
    tr.appendChild(titleTd);

    const privacyTd = document.createElement("td");
    const privacySelect = document.createElement("select");
    for (const [value, label] of Object.entries(PRIVACY_LABEL)) {
      const opt = document.createElement("option");
      opt.value = value;
      opt.textContent = label;
      if (value === v.privacyStatus) opt.selected = true;
      privacySelect.appendChild(opt);
    }
    privacySelect.addEventListener("change", () => tr.classList.add("dirty"));
    privacyTd.appendChild(privacySelect);
    tr.appendChild(privacyTd);

    const uploadStatusTd = document.createElement("td");
    uploadStatusTd.textContent = v.uploadStatus || "";
    tr.appendChild(uploadStatusTd);

    const likeCountTd = document.createElement("td");
    likeCountTd.textContent = v.likeCount != null ? v.likeCount : "-";
    tr.appendChild(likeCountTd);

    const saveTd = document.createElement("td");
    const saveBtn = document.createElement("button");
    saveBtn.textContent = "保存";
    const resultSpan = document.createElement("span");
    const doSave = (precomputedCurrent) =>
      saveRow(tr, v, titleInput, privacySelect, saveBtn, resultSpan, precomputedCurrent);
    // addEventListenerはクリックイベント自体を第1引数として渡してくるので、
    // doSaveへそのまま渡すとprecomputedCurrentにEventオブジェクトが紛れ込んでしまう。
    // 単発クリック時は必ず引数なしで呼ぶ。
    saveBtn.addEventListener("click", () => doSave());
    // 「まとめて保存」からもこの行を保存できるように参照を持たせておく
    tr._save = doSave;
    saveTd.appendChild(saveBtn);
    saveTd.appendChild(resultSpan);
    tr.appendChild(saveTd);

    tbody.appendChild(tr);
  }

  updateSelectedCount();
}

async function saveRow(tr, v, titleInput, privacySelect, saveBtn, resultSpan, precomputedCurrent) {
  saveBtn.disabled = true;
  resultSpan.textContent = "確認中...";
  resultSpan.className = "";
  try {
    // 保存前に、この動画だけ現在の実際の状態を確認する。
    // キャッシュ取得後にYouTube Studio側などで直接変更されていた場合、
    // 気づかず上書きしてしまうのを防ぐ。
    // 「まとめて保存」からは事前にバッチ確認済みの結果(precomputedCurrent)が渡ってくるので
    // ここで個別に確認せず、単発の「保存」ボタン押下時だけ1件確認する(1 unit)。
    let current = precomputedCurrent;
    if (!current) {
      const currentRes = await fetch(`/api/videos/${v.id}/current`);
      current = await currentRes.json();
      if (!current.ok) throw new Error(current.error || "現在の状態の確認に失敗したよ");
    }
    // サーバーが不安定だった等で必要な項目が欠けてる場合、紛らわしい"undefined"表示で
    // 確認ダイアログを出すよりも、はっきりエラーとして扱う（サーバー再起動直後などに発生しうる）
    if (current.title === undefined || current.privacyStatus === undefined) {
      throw new Error("現在の状態がうまく取得できなかったよ。もう一度「保存」を押してみてね");
    }

    const titleChanged = current.title !== v.title;
    const privacyChanged = current.privacyStatus !== v.privacyStatus;
    if (titleChanged || privacyChanged) {
      const lines = ["キャッシュ取得後に、YouTube側で内容が変わってるみたい！"];
      if (titleChanged) {
        lines.push(`タイトル: 現在「${current.title}」 / キャッシュ「${v.title}」`);
      }
      if (privacyChanged) {
        lines.push(
          `公開設定: 現在「${PRIVACY_LABEL[current.privacyStatus] || current.privacyStatus}」 / キャッシュ「${PRIVACY_LABEL[v.privacyStatus] || v.privacyStatus}」`
        );
      }
      lines.push("このまま今の編集内容で上書き保存する？（キャンセルすると保存しないよ）");
      if (!confirm(lines.join("\n"))) {
        resultSpan.textContent = "保存キャンセルしたよ";
        resultSpan.className = "rowError";
        return false;
      }
    }

    resultSpan.textContent = "保存中...";
    const res = await fetch(`/api/videos/${v.id}`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        title: titleInput.value,
        privacyStatus: privacySelect.value,
      }),
    });
    const data = await res.json();
    if (!data.ok) throw new Error(data.error || "保存に失敗したよ");
    v.title = titleInput.value;
    v.privacyStatus = privacySelect.value;
    tr.classList.remove("dirty");
    resultSpan.textContent = "保存したよ";
    resultSpan.className = "rowOk";
    saveCache();
    return true;
  } catch (e) {
    resultSpan.textContent = e.message;
    resultSpan.className = "rowError";
    return false;
  } finally {
    saveBtn.disabled = false;
  }
}

async function saveAllDirtyRows() {
  const dirtyRows = Array.from(tbody.querySelectorAll("tr.dirty"));
  if (dirtyRows.length === 0) {
    alert("変更されてる行がないよ！タイトルや公開設定を編集してから押してね");
    return;
  }
  if (!confirm(`編集した${dirtyRows.length}件をまとめて保存するよ。よかった？`)) {
    return;
  }

  saveAllBtn.disabled = true;
  try {
    // 保存前チェックをバッチ化：対象の動画IDを50件ずつまとめて確認する
    // （1件ずつ確認するとN unitsかかるところを、ceil(N/50) unitsに圧縮）
    statusEl.textContent = "保存前チェック中...";
    const ids = dirtyRows.map((tr) => tr.dataset.id);
    const currentStates = {};
    for (let i = 0; i < ids.length; i += 50) {
      const chunk = ids.slice(i, i + 50);
      const res = await fetch("/api/videos/check_many", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ ids: chunk }),
      });
      const data = await res.json();
      if (!data.ok) throw new Error(data.error || "保存前チェックに失敗したよ");
      Object.assign(currentStates, data.states);
    }

    let successCount = 0;
    for (let i = 0; i < dirtyRows.length; i++) {
      statusEl.textContent = `まとめて保存中... (${i + 1}/${dirtyRows.length})`;
      const id = dirtyRows[i].dataset.id;
      const ok = await dirtyRows[i]._save(currentStates[id]);
      if (ok) successCount++;
    }
    statusEl.textContent =
      successCount === dirtyRows.length
        ? `${successCount}件まとめて保存できたよ🎉`
        : `${successCount}/${dirtyRows.length}件保存できたよ（失敗した行はエラーメッセージ見てね）`;
  } catch (e) {
    statusEl.textContent = `エラー: ${e.message}`;
  } finally {
    saveAllBtn.disabled = false;
  }
}

function getSelectedIds() {
  return Array.from(
    tbody.querySelectorAll('input[type="checkbox"][data-id]:checked')
  ).map((cb) => cb.dataset.id);
}

function updateSelectedCount() {
  selectedCountEl.textContent = `${getSelectedIds().length}件選択中`;
}

async function bulkApply() {
  const ids = getSelectedIds();
  if (ids.length === 0) {
    alert("動画を選択してね！");
    return;
  }
  const privacyStatus = bulkPrivacySelect.value;
  if (!privacyStatus) {
    alert("適用先で「公開設定は変更しない」以外を選んでね！");
    return;
  }
  if (
    !confirm(
      `${ids.length}件の動画を「${PRIVACY_LABEL[privacyStatus]}」に変更するよ。よかった？`
    )
  ) {
    return;
  }

  bulkApplyBtn.disabled = true;
  statusEl.textContent = "一括適用中...";
  try {
    const res = await fetch("/api/videos/bulk_privacy", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ ids, privacyStatus }),
    });
    const data = await res.json();
    const failed = data.results.filter((r) => !r.ok);
    for (const r of data.results) {
      if (r.ok) {
        const v = videos.find((x) => x.id === r.id);
        if (v) v.privacyStatus = privacyStatus;
      }
    }
    saveCache();
    renderTable();
    statusEl.textContent =
      failed.length === 0
        ? `${ids.length}件すべて更新できたよ🎉`
        : `${ids.length - failed.length}件成功、${failed.length}件失敗したよ`;
  } catch (e) {
    statusEl.textContent = `エラー: ${e.message}`;
  } finally {
    bulkApplyBtn.disabled = false;
  }
}
