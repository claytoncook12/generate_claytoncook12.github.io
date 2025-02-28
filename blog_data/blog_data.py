from blog_data.model.blog import Blog

blog_posts: list[Blog] = [
    Blog(
        "Graphing with Django and Plotly",
        "Febuary 28, 2025",
        """Graphing with Django and Plotly is a powerful combination for creating interactive and visually
        appealing graphs on the web. In this blog post, we will explore plotting with plotly on the
        client or server side.""",
        "chart_image.jpg",
        "Generated with AI February 28, 2025 at 11:56 AM",
        ['Django','Plotly','Graphing',"Python","Javascript"],
        "Graphing_with_Django_and_Plotly.html"
    ),
    Blog(
        "Takeaways from TRB 2025",
        "January 15, 2025",
        "Reflecting on my first TRB Confrence in Washington, DC from Dec. 5-8, 2025.",
        "trb2025_confrence_hall.jpg",
        "",
        ['TRB','Civil','Pavement','Geotechnology'],
        "TRB_2025_Summary.html"
    ),
    Blog(
        "Boat Ramp Civil Drawing Creation",
        "October 29, 2024",
        """A collections of a few videos that covers the highlights of creating
        a set of drawings for a boat ramp extension with AutoCad and Carlson
        Civil 2024 suite..""",
        "alexander_ramp_green_river.jpg",
        '',
        ['Civil','AutoCad','Carlson','Plans'],
        "Boat_Ramp_Civil_Drawing_Creation.html"
    ),
    Blog(
        "Creating An Aerial Image From A Drone Flight for Civil Drawings",
        "October 25, 2024",
        """In this recording, I go through the process of creating an aerial image using DroneLink, WebODM Lightning,
        AutoCAD 2024 with the Carlson Civil suite for civil engineering drawings.""",
        "dam_5_ramp_image.jpg",
        '',
        ['Civil','AutoCad','Carlson','Drone'],
        "Drone_Aerial_Image_Creation.html"
    ),
    Blog(
        "Creating A Staking Plan with AutoCad And Carlson Civil 2024",
        "October 24, 2024",
        """In this recording, I go through the process of creating a staking plan using AutoCAD 2024 with the Carlson Civil suite
        for staking in the field.""",
        "Hinkston-Boat-Ramp.jpg",
        '',
        ['Civil','AutoCad','Carlson','Staking'],
        "Staking_Plan_Creation.html"
    ),
    Blog(
        "Traditional Irish Melodies Workshop March 24th, 2024 Resources",
        "March 27, 2024",
        """Traditional Irish Melodies workshop at the Louisville Folk School.
        Talked about the banjo in irish music, fathers of the
        irish banjo and taught some irish tunes. Within the blog post are some reference audio
        files as well.""",
        "ira-selendripity-qUpzRaylopM-unsplash.jpg",
        'Photo by <a href="https://unsplash.com/@selendripity?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Ira Selendripity</a> on <a href="https://unsplash.com/photos/brown-string-instrument-qUpzRaylopM?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>',
        ['Irish Music','Fiddle','Banjo'],
        "Traditional_Irish_Melodies_Workshop_March_24th_2024_Resources.html"
    ),
    Blog(
        "The Observer Pattern and Reactive Programming",
        "June 22, 2023",
        """In order to better under stand the observer pattern and reactive programming
        I wanted to write a observer in javascript and explorer some common features in
        vanilla RxJS project with WebPack.
        """,
        "good-free-photos-LADl0hVNBCQ-unsplash.jpg",
        'Photo by <a href="https://unsplash.com/@goodfreephoto_com?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Good Free Photos</a> on <a href="https://unsplash.com/photos/LADl0hVNBCQ?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>',
        ['Observer Pattern','Reactive Programming','Javascript'],
        "observer_pattern_and_reactive_programming.html"
    ),
    Blog(
        "Rescaling Video Files with FFmpeg to Maximizing an Older iPod",
        "May 30, 2023",
        """My daughter was give an older iPod touch fourth-generation with 6.4 Gb of storage. In an
        effort to maximize the amount of videos that I could fit on the device I turned to using
        FFmpeg to reduce the mp4 video files down to a resolution that was watchable on the iPod. I found
        that I could get roughly 7.31 hrs of video per 1 GB.""",
        "ross-parmly-rf6ywHVkrlY-unsplash.jpg",
        'Photo by <a href="https://unsplash.com/@rparmly?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Ross Parmly</a> on <a href="https://unsplash.com/photos/rf6ywHVkrlY?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>',
        ['FFmpeg'],
        "maximizing-an-older-ipod.html"
    ),
    Blog(
        "Using Interfaces to Ensure Behavior",
        "Febuary 23, 2023",
        """Interfaces ensure that a class behaves in a certain way and expresses
        polymorphism between different classes. We will look at how to implement
        interfaces in C#, Python, and Typescript.""",
        "ganapathy-kumar-L75D18aVal8-unsplash.jpg",
        'Photo by <a href="https://unsplash.com/@gkumar2175?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Ganapathy Kumar</a> on <a href="https://unsplash.com/images/nature/desert?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>',
        ['Interface', 'Protocol','C#','Python','Typescript'],
        "using-interfaces-to-insure-behavior.html"
    ),
    Blog(
        "Introduction of Database Design and Entity Framework Core 2.2.1",
        "February 16, 2023",
        """An overview of general database design principles, how to use Entity Framework Core 
        and connect up to a local SQLite database.""",
        "michael-benz--IZ2sgQKIhM-unsplash.jpg",
        'Photo by <a href="https://unsplash.com/@michaelbenz?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Michael Benz</a> on <a href="https://unsplash.com/wallpapers/nature/forest?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>',
        ['.NET', 'C#', 'Database'],
        "entity-framework-core-introduction.html"
    ),
    Blog(
        "Combining MP3 Files with Python and FFmpeg",
        "February 13, 2023",
        "A short python script to easily add together mp3 files.",
        "daniel-schludi-mbGxz7pt0jM-unsplash.jpg",
        'Photo by <a href="https://unsplash.com/@schluditsch?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Daniel Schludi</a> on <a href="https://unsplash.com/photos/mbGxz7pt0jM?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>',
        ['Python', 'FFmpeg'],
        "combining-mp3-file-with-python-and-ffmpeg.html"
    ),
    Blog(
        "Shared Custom Angular Form Validation Through A Service",
        "November 1, 2022",
        "Setting up shared custom model validation through an angular service.",
        "clem-onojeghuo--YMhg0KYgVc-unsplash.jpg",
        'Photo by <a href="https://unsplash.com/@clemono?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Clem Onojeghuo</a> on <a href="https://unsplash.com/s/photos/nature-free?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>',
        ["Programming", "Angular", "Testing"],
        "shared-custom-angular-form-validation-through-a-service.html"
    ),
    Blog(
        "Setting Up A Python Project",
        "October 24, 2022",
        "Quick reference for command line commands I use for setting up a python project.",
        "luca-bravo-lWAOc0UuJ-A-unsplash.jpg",
        'Photo by <a href="https://unsplash.com/@lucabravo?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Luca Bravo</a> on <a href="https://unsplash.com/?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>',
        ["Programming", "Python"],
        "setting-up-a-python-project.html"
    )
]