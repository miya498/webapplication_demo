document.addEventListener("DOMContentLoaded", function() {
    const newReportForm = document.getElementById("new-report-form");
    const reportList = document.getElementById("report-list");

    // 新しい報告書フォームの送信イベント
    newReportForm.addEventListener("submit", function(event) {
        event.preventDefault(); // デフォルトのフォーム送信を防止

        // フォームの値を取得
        const title = document.getElementById("report-title").value;
        const date = document.getElementById("report-date").value;
        const content = document.getElementById("report-content").value;

        // 新しい報告書を作成
        const newReport = document.createElement("li");
        newReport.innerHTML = `
            <strong>${title}</strong> - ${date}<br>
            ${content}
        `;

        // 報告書一覧に追加
        reportList.appendChild(newReport);

        // フォームをリセット
        newReportForm.reset();
    });
});
