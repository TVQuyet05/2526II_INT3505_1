async function runClient() {
  try {
    const SERVER_URL = "http://localhost:3000";

    // 1. Lấy dữ liệu điểm số
    console.log("-> Đang lấy danh sách điểm...");
    const responseData = await fetch(`${SERVER_URL}/api/scores`);
    const scores = await responseData.json();
    console.log("1. Danh sách điểm:", scores);

    // 2. Lấy logic xếp loại (Code-on-Demand)
    console.log("-> Đang tải logic xếp loại...");
    const responseCode = await fetch(`${SERVER_URL}/api/logic`);
    const logicScript = await responseCode.text();
    console.log("2. Code nhận được:", logicScript);

    // 3. Thực thi code tải về
    // eval() sẽ định nghĩa hàm classify(score) trong scope hiện tại
    eval(logicScript);

    // 4. Áp dụng logic lên từng điểm số
    console.log("3. Kết quả xếp loại:");
    scores.forEach((score) => {
      // @ts-ignore
      if (typeof classify === "function") {
        const result = classify(score);
        console.log(`- Điểm ${score} => ${result}`);
      }
    });
  } catch (error) {
    console.error("Lỗi:", error.message);
  }
}

runClient();
