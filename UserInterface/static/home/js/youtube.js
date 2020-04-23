/*
function onYouTubeIframeAPIReady() {
    var muteYouTubeVideoPlayer;
    muteYouTubeVideoPlayer = new YT.Player('muteYouTubeVideoPlayer', {
        videoId: '4wFlJHVcBKs', // YouTube Video ID
        width: 600,               // Player width (in px)
        height: 470,              // Player height (in px)
        playerVars: {
        autoplay: 1,        // Auto-play the video on load
        controls: 0,        // Show pause/play buttons in player
        showinfo: 1,        // Hide the video title
        modestbranding: 0,  // Hide the Youtube Logo
        loop: 0,            // Run the video in a loop
        fs: 0,              // Hide the full screen button
        cc_load_policy: 0, // Hide closed captions
        iv_load_policy: 3,  // Hide the Video Annotations
        autohide: 0         // Hide video controls when playing
        },
        events: {
        onReady: function(e) {
            e.target.mute();
        }
        }
    })
    var muteLiveViewEarthE;
    muteLiveViewEarthE = new YT.Player('muteLiveViewEarthE', {
        videoId: 'zSRs9Y7lprk', // YouTube Video ID
        width: 480,               // Player width (in px)
        height: 360,              // Player height (in px)
        playerVars: {
            autoplay: 1,        // Auto-play the video on load
            controls: 0,        // Show pause/play buttons in player
            showinfo: 1,        // Hide the video title
            modestbranding: 0,  // Hide the Youtube Logo
            loop: 1,            // Run the video in a loop
            fs: 0,              // Hide the full screen button
            cc_load_policy: 0, // Hide closed captions
            iv_load_policy: 3,  // Hide the Video Annotations
            autohide: 0         // Hide video controls when playing
        },
        events: {
            onReady: function(e) {
                e.target.mute();
            }
        }
    })
    var muteEarthE;
    muteEarthE = new YT.Player('muteEarthE', {
        videoId: 'zSRs9Y7lprk', // YouTube Video ID
        width: 480,               // Player width (in px)
        height: 360,              // Player height (in px)
        playerVars: {
            autoplay: 1,        // Auto-play the video on load
            controls: 0,        // Show pause/play buttons in player
            showinfo: 1,        // Hide the video title
            modestbranding: 0,  // Hide the Youtube Logo
            loop: 0,            // Run the video in a loop
            fs: 0,              // Hide the full screen button
            cc_load_policy: 0, // Hide closed captions
            iv_load_policy: 3,  // Hide the Video Annotations
            autohide: 0         // Hide video controls when playing
        },
        events: {
            onReady: function(e) {
                e.target.mute();
            }
        }
    })
    var muteSortRig;
    muteSortRig = new YT.Player('muteSortRig', {
        videoId: 'zSRs9Y7lprk', // YouTube Video ID
        width: 480,               // Player width (in px)
        height: 360,              // Player height (in px)
        playerVars: {
            autoplay: 1,        // Auto-play the video on load
            controls: 0,        // Show pause/play buttons in player
            showinfo: 1,        // Hide the video title
            modestbranding: 0,  // Hide the Youtube Logo
            loop: 1,            // Run the video in a loop
            fs: 0,              // Hide the full screen button
            cc_load_policy: 0, // Hide closed captions
            iv_load_policy: 3,  // Hide the Video Annotations
            autohide: 0         // Hide video controls when playing
        },
        events: {
            onReady: function(e) {
                e.target.mute();
            }
        }
    })
    var muteEyeInTheSky;
    muteEyeInTheSky = new YT.Player('muteEyeInTheSky', {
        videoId: 'zSRs9Y7lprk', // YouTube Video ID
        width: 480,               // Player width (in px)
        height: 360,              // Player height (in px)
        playerVars: {
            autoplay: 1,        // Auto-play the video on load
            controls: 0,        // Show pause/play buttons in player
            showinfo: 1,        // Hide the video title
            modestbranding: 0,  // Hide the Youtube Logo
            loop: 1,            // Run the video in a loop
            fs: 0,              // Hide the full screen button
            cc_load_policy: 0, // Hide closed captions
            iv_load_policy: 3,  // Hide the Video Annotations
            autohide: 0         // Hide video controls when playing
        },
        events: {
            onReady: function(e) {
                e.target.mute();
            }
        }
    })
}