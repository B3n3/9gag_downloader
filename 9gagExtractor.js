/**
 * Downloads a csv String into a file.
 * @param csvString the whole content of the CSV to be downloaded
 */
const download_b3n3_9gag_csv = function (csvString) {
    const filename = '9gag_exports_' + new Date().toLocaleDateString() + '.csv';
    const link = document.createElement('a');
    link.style.display = 'none';
    link.setAttribute('target', '_blank');
    link.setAttribute('href', 'data:text/csv;charset=utf-8,' + encodeURIComponent(csvString));
    link.setAttribute('download', filename);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
};

// Perform the actual download.
download_b3n3_9gag_csv(Array.from(b3n3_9gag_downloader_csv).join('\n'));
