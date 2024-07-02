"""Generates Website"""

import os, shutil
from jinja2 import Template, Environment, FileSystemLoader


from blog_data.model.blog import Blog, Tag
from blog_data.blog_data import blog_posts

class SiteGenerator(object):
    def __init__(self):
        self.env = Environment(
            loader=FileSystemLoader('template')
        )

        self.css_style_sheets: list[str] = ["w3.css"]
        self.head_shot: str = "csc_headshot_2.jpg"
        self.blog_posts: list[Blog] = blog_posts
        self.main_blog_posts: list[str] = []
        self.tags: dict[str, str] = dict()

        # Actions To Generate Site
        self.empty_public()
        self.copy_static()
        self.create_public_blog_folder()
        self.create_public_tag_folder()
        self.set_main_blog_posts()
        self.render_about_page()
        self.render_music_page()
        self.render_favorites_page()
        self.render_cadd_page()
        self.collect_blog_post_tags()
        self.render_main_page()
        self.render_blog_posts()
        self.render_tag_pages()
        self.html_projects_copy()
        self.finished()
    
    def empty_public(self) -> None:
        """ Ensure the public directory is empty before generating. """
        try:
            shutil.rmtree('./public') 
            os.mkdir('./public')
        except:
            print("Error cleaning up old files.")
    
    def copy_static(self) -> None:
        """ Copy static assets to the public directory """
        try:
            shutil.copytree('template/static', 'public/static')
        except:
            print("Error copying static files.")
    
    def create_public_blog_folder(self) -> None:
        try:
            os.mkdir('./public/blog')
        except:
            print("Error Creating Blog Post folder.")
    
    def create_public_tag_folder(self) -> None:
        try:
            os.mkdir('./public/tag')
        except:
            print("Error Creating Tag folder.")
    
    def set_main_blog_posts(self) -> None:
        """ Sets Main Blog Posts From  blog_post list"""
        self.main_blog_posts.append(blog_posts[0])

    def collect_blog_post_tags(self) -> None:
        """ Collect All Tags in Blog Posts """
        try:
            temp_tags = dict()
            for blog in blog_posts:
                for tag in blog.tags:
                    if str(tag) not in temp_tags:
                        temp_tags[str(tag)] = [blog]
                    else:
                        temp_tags[str(tag)] = temp_tags[str(tag)] + [blog]
            
            ## Convert string Key to Tag Obj 
            for key, value in temp_tags.items():
                self.tags[Tag(key)] = value

        except:
            raise Exception(f"Error collecting tags.")
    
    def render_main_page(self) -> None:
        """ Create Index Page """
        print("Rendering Main page to static file.")
        template = self.env.get_template('_index.html')
        with open('public/index.html', 'w+') as file:
            html = template.render(
                css_style_sheets = self.css_style_sheets,
                blog_posts = self.blog_posts,
                main_blog_posts = self.main_blog_posts,
                tags = self.tags
            )
            file.write(html)
    
    def render_about_page(self) -> None:
        """ Create About Page """
        print("Rendering About page to static files")
        template = self.env.get_template('_about.html')
        with open('public/about.html', 'w+') as file:
            html = template.render(
                css_style_sheets = self.css_style_sheets,
                head_shot = self.head_shot,
            )
            file.write(html)
    
    def render_music_page(self) -> None:
        """ Create Music Page """
        print("Rendering About page to static files")
        template = self.env.get_template('_music.html')
        with open('public/music.html', 'w+') as file:
            html = template.render(
                css_style_sheets = self.css_style_sheets,
                head_shot = self.head_shot,
            )
            file.write(html)
    
    def render_favorites_page(self) -> None:
        """ Create Favorite Links Page """
        print("Rendering Favorite Links page to static files")
        template = self.env.get_template('_favorite_links.html')
        with open('public/favorite_links.html', 'w+') as file:
            html = template.render(
                css_style_sheets = self.css_style_sheets
            )
            file.write(html)
    
    def render_cadd_page(self) -> None:
        """ Create Autocadd and Carlson Learning Page """
        print("Rendering Autocadd and Carlson Learning Page page to static files")
        template = self.env.get_template('_cadd.html')
        with open('public/cadd.html', 'w+') as file:
            html = template.render(
                css_style_sheets = self.css_style_sheets
            )
            file.write(html)

    def render_blog_posts(self) -> None:
        """ Render Blog Post Pages """
        print("Rendering Blog post pages")
        
        for blog_post in blog_posts:
            template = self.env.get_template('blog/_blog.html')
            try:
                blog_file_name = blog_post.html_file
            except:
                raise Exception(f"{blog_post} needs an html_file set.")
            blog_file_contents = ""
            print(f"Creating {blog_file_name}")

            # Read in Blog Html Text
            with open('blog_data/html_files/' + blog_file_name, 'r') as file:
                blog_file_contents = file.read()

            # Write Blog Post Files
            with open('public/blog/' + blog_file_name, 'w+') as file:
                html = template.render(
                    css_style_sheets = self.css_style_sheets + ['clayton-cook-website.css'],
                    index_ref = "../",
                    blog_post = blog_post,
                    blog_file_contents = blog_file_contents
                )
                file.write(html)
    
    def render_tag_pages(self) -> None:
        """ Render Tag Pages """
        print("Rendering Tag Pages")

        for tag, blog_posts in self.tags.items():
            template = self.env.get_template('tag/_tag.html')
            try:
                file_name = tag.tag_slug() + ".html"
            except:
                raise Exception(f"Error with setting {tag} html file name")
            print(f"Creating {file_name}")

            # Write Tag Files
            with open('public/tag/' + file_name, 'w+') as file:
                html = template.render(
                    css_style_sheets = self.css_style_sheets + ['clayton-cook-website.css'],
                    index_ref = "../",
                    tag = tag,
                    blog_posts = blog_posts
                )
                file.write(html)
        

    def html_projects_copy(self) -> None:
        """ Move HTML Projects From Folder to public """
        try:
            shutil.copytree('html_projects/', 'public/html_projects')
        except:
            print("Error copying html project files.")    
    
    def finished(self) -> None:
        """ Finished Message """
        print("Finished webpage creation.")

if __name__ == "__main__":
    SiteGenerator()