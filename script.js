// Hàm lấy dữ liệu từ file JSON
async function fetchData() {
    const response = await fetch('data.json');
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    return await response.json();
}

// Hàm kiểm tra xem từ có hợp lệ không
function isValidWord(word, wordsData) {
    for (const tone in wordsData) {
        for (const category in wordsData[tone]) {
            // Kiểm tra cả chữ hoa và chữ thường
            if (wordsData[tone][category].includes(word.toLowerCase()) || wordsData[tone][category].includes(word)) {
                return true;
            }
        }
    }
    return false;
}

// Hàm tạo từ hợp lệ từ input
function generateWords(input, wordsData) {
    // Giữ lại các ký tự có dấu và loại bỏ dấu "/" và khoảng trắng
    const cleanedInput = input.replace(/[/\s]/g, '');
    
    const chars = cleanedInput.split('');
    const results = [];

    console.log("Cleaned input:", cleanedInput);  // Log input sau khi làm sạch

    function combineWords(current, remaining) {
        if (current.length > 0 && isValidWord(current, wordsData)) {
            results.push(current);
            console.log("Valid word found:", current);  // Log từ hợp lệ tìm thấy
        }
        if (current.length < 6) {
            for (let i = 0; i < remaining.length; i++) {
                const nextCurrent = current + remaining[i];
                const nextRemaining = remaining.filter((_, index) => index !== i);
                combineWords(nextCurrent, nextRemaining);
            }
        }
    }

    combineWords('', chars);
    return results;
}

// Hàm chính xử lý đầu vào và xuất ra kết quả
async function main(input) {
    const wordsData = await fetchData();
    const validWords = generateWords(input, wordsData);
    const output = [];
    const inputLength = input.replace(/[/\s]/g, '').length; // Số ký tự tính từng chữ

    console.log("Valid words:", validWords);  // Log danh sách từ hợp lệ tìm thấy

    // Tạo ra các cặp từ không trùng ký tự
    for (let i = 0; i < validWords.length; i++) {
        for (let j = 0; j < validWords.length; j++) {
            if (i !== j) {
                const combined = `${validWords[i]} ${validWords[j]}`;
                const combinedLength = combined.replace(/\s+/g, '').length; // Đếm ký tự không khoảng trắng
                const combinedChars = combined.replace(/\s+/g, '').split('');
                const inputChars = input.replace(/[/\s]/g, '').split('');

                console.log("Checking combination:", combined);  // Log quá trình kiểm tra tổ hợp

                // Kiểm tra xem mỗi ký tự chỉ được sử dụng 1 lần trong cặp từ
                if (combinedLength === inputLength && combinedChars.every(char => inputChars.includes(char))) {
                    const inputCharsCopy = [...inputChars];
                    let validCombination = true;

                    for (const char of combinedChars) {
                        const index = inputCharsCopy.indexOf(char);
                        if (index !== -1) {
                            inputCharsCopy.splice(index, 1); // Xóa ký tự khỏi mảng để tránh trùng lặp
                        } else {
                            validCombination = false;
                            break;
                        }
                    }

                    if (validCombination) {
                        output.push(combined);
                        console.log("Valid combination found:", combined);  // Log tổ hợp hợp lệ tìm thấy
                    }
                }
            }
        }
    }

    return output.length > 0 ? output : ["Không có kết quả nào."];
}

// Xử lý sự kiện khi người dùng nhấn nút
document.getElementById('findButton').addEventListener('click', async () => {
    const input = document.getElementById('inputField').value;
    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = "Đang tìm kiếm..."; // Hiển thị trạng thái tìm kiếm

    console.log("Input:", input);  // Log đầu vào

    try {
        const results = await main(input);
        console.log("Results:", results);  // Log kết quả tìm kiếm
        resultDiv.innerHTML = results.join('<br>'); // Hiển thị kết quả
    } catch (error) {
        console.error('Error fetching data:', error);
        resultDiv.innerHTML = "Có lỗi xảy ra khi tìm kiếm.";
    }
});

//Ending