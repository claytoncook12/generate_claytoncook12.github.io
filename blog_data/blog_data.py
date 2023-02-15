from blog_data.model.blog import Blog

blog_posts: list[Blog] = [
    Blog(
        "Introduction of Database Design and Entity Framework Core 2.2.1",
        "NEED DATE",
        """An overview of general database design principles, how to use Entity Framework Core 
        and connect up to a local SQLite database.""",
        "michael-benz--IZ2sgQKIhM-unsplash.jpg",
        'Photo by <a href="https://unsplash.com/@michaelbenz?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Michael Benz</a> on <a href="https://unsplash.com/wallpapers/nature/forest?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>',
        ['DotNET', 'C-Sharp', 'Database'],
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