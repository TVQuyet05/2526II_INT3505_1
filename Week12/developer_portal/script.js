// Dummy script để giả lập UI tương tác
let currentApiKey = "";

function generateApiKey() {
  const btn = document.getElementById("generateBtn");
  btn.innerHTML =
    '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Đang tạo...';
  btn.disabled = true;

  // Giả lập network delay
  setTimeout(() => {
    // Sinh 1 token ngẫu nhiên
    const prefix = "bookapi_test_";
    const randomString =
      Math.random().toString(36).substring(2, 15) +
      Math.random().toString(36).substring(2, 15);
    currentApiKey = prefix + randomString;

    const inputField = document.getElementById("apiKeyDisplay");
    inputField.value = currentApiKey;

    btn.innerHTML = '<i class="bi bi-arrow-clockwise"></i> Tạo lại Token';
    btn.disabled = false;

    // Hiển thị toast hoặc alert (dùng alert cho nhanh chóng ở mẫu demo)
    alert("Tạo API Key thành công! Hãy lưu lại để sử dụng.");
  }, 800);
}

function copyApiKey() {
  const copyText = document.getElementById("apiKeyDisplay");

  if (!copyText.value || copyText.value === "Chưa được tạo...") {
    alert("Vui lòng tạo API Key trước!");
    return;
  }

  // Chọn text
  copyText.select();
  copyText.setSelectionRange(0, 99999); // Mobile

  // Copy
  navigator.clipboard.writeText(copyText.value).then(() => {
    alert("Đã sao chép API Key: " + copyText.value);
  });
}
