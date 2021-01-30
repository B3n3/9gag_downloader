/**
 * Pulls posts every 0.5 seconds from the website and stores them into a global variable.
 */
setInterval(function () {
    const articles = document.querySelectorAll('article');
    window.b3n3_9gag_downloader_csv = window.b3n3_9gag_downloader_csv || new Set();
    for (let i = 0; i < articles.length; i++) {
        const e = articles[i];
        let header = e.querySelector('header h1');
        if (header !== null) {
            header = header.textContent.split(',').join('_');

            const video = e.querySelector('video source');
            let videoSrc;
            if (video !== null) {
                videoSrc = video.src;
                let csvImage = header + ',' + videoSrc;
                if (!b3n3_9gag_downloader_csv.has(csvImage)) {
                    console.log('Video', header, videoSrc);
                    b3n3_9gag_downloader_csv.add(csvImage);
                }
            }

            const img = e.querySelector('.post-container picture > source');
            let imgSrc;
            if (img !== null) {
                imgSrc = img.srcset;
                let csvVideo = header + ',' + imgSrc;
                if (!b3n3_9gag_downloader_csv.has(csvVideo)) {
                    console.log('Image', header, imgSrc);
                    b3n3_9gag_downloader_csv.add(csvVideo);
                }
            }
        }
    }
}, 500);