(function () {
    /**
     * Downloads a csv String into a file.
     * @param csvString the whole content of the CSV to be downloaded
     */
    const download = function (csvString) {
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

    const articles = document.querySelectorAll('article');
    const csv = [];
    for (let i = 0; i < articles.length; i++) {
        const e = articles[i];
        let header = e.querySelector('header h1');
        if (header !== null) {
            header = header.textContent.split(',').join('_');

            const video = e.querySelector('video source');
            let videoSrc;
            if (video !== null) {
                videoSrc = video.src;
                console.log('Video', header, videoSrc);
                csv.push(header + ',' + videoSrc);
            }

            const img = e.querySelector('.post-container picture > source');
            let imgSrc;
            if (img !== null) {
                imgSrc = img.srcset;
                console.log('Image', header, imgSrc);
                csv.push(header + ',' + imgSrc);
            }
        }
    }

    download(csv.join('\n'));
})();
