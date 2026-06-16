const dropZone = document.getElementById('drop-zone');
const fileInput = document.getElementById('file-input');
const loading = document.getElementById('loading');
const results = document.getElementById('results');

// Handle drag and drop visuals
dropZone.addEventListener('dragover', (e) => {
    e.preventDefault();
    dropZone.classList.add('dragover');
});

dropZone.addEventListener('dragleave', () => dropZone.classList.remove('dragover'));

dropZone.addEventListener('drop', (e) => {
    e.preventDefault();
    dropZone.classList.remove('dragover');
    if (e.dataTransfer.files.length) {
        handleFile(e.dataTransfer.files[0]);
    }
});

fileInput.addEventListener('change', (e) => {
    if (e.target.files.length) {
        handleFile(e.target.files[0]);
    }
});

async function handleFile(file) {
    // Reset UI
    results.classList.add('hidden');
    dropZone.classList.add('hidden');
    loading.classList.remove('hidden');

    const formData = new FormData();
    formData.append("file", file);

    try {
        const response = await fetch("http://127.0.0.1:8000/upload", {
            method: "POST",
            body: formData
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.detail || "Failed to process document");
        }

        const data = await response.json();
        
        // Populate Data
        document.getElementById('res-name').textContent = data.filename;
        document.getElementById('res-type').textContent = data.file_type;
        document.getElementById('res-words').textContent = data.word_count;
        document.getElementById('res-summary').textContent = data.summary;

        // Show Results
        loading.classList.add('hidden');
        results.classList.remove('hidden');

    } catch (error) {
        alert("Error: " + error.message);
        loading.classList.add('hidden');
        dropZone.classList.remove('hidden'); // Reset UI to try again
    }
}