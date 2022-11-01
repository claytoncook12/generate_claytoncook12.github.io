"""Generates Website"""

import os, shutil
from datetime import datetime
from jinja2 import Template, Environment, FileSystemLoader

from blog_data.blog_data import blog_posts

class SiteGenerator(object):
    def __init__(self):
        self.env = Environment(
            loader=FileSystemLoader('template')
        )

        self.css_style_sheets = ["w3.css"]
        self.head_shot = "csc_headshot.svg"
        self.blog_posts = blog_posts
        self.main_blog_posts = []
        self.tags = set()

        # Actions To Generate Site
        self.empty_public()
        self.copy_static()
        self.create_public_blog_folder()
        self.set_main_blog_posts()
        self.collect_blog_post_tags()
        self.render_main_page()
        self.render_blog_posts()
        self.finished()
    
    def empty_public(self):
        """ Ensure the public directory is empty before generating. """
        try:
            shutil.rmtree('./public') 
            os.mkdir('./public')
        except:
            print("Error cleaning up old files.")
    
    def copy_static(self):
        """ Copy static assets to the public directory """
        try:
            shutil.copytree('template/static', 'public/static')
        except:
            print("Error copying static files.")
    
    def create_public_blog_folder(self):
        try:
            os.mkdir('./public/blog')
        except:
            print("Error Creating Blog Post folder.")
    
    def set_main_blog_posts(self):
        """ Sets Main Blog Posts From  blog_post list"""
        self.main_blog_posts.append(blog_posts[0])

    def collect_blog_post_tags(self):
        """ Collect All Tags in Blog Posts """
        try:
            for blog in blog_posts:
                for tag in blog["tags"]:
                    self.tags.add(tag)
        except:
            print("Error collecting tags.")
    
    def render_main_page(self):
        """ Create Index Page """
        print("Rendering Main page to static file.")
        template = self.env.get_template('_index.html')
        with open('public/index.html', 'w+') as file:
            html = template.render(
                css_style_sheets = self.css_style_sheets,
                head_shot = self.head_shot,
                blog_posts = self.blog_posts,
                main_blog_posts = self.main_blog_posts,
                tags = self.tags
            )
            file.write(html)

    def render_blog_posts(self):
        """ Render Blog Post Pages """
        print("Rendering Blog post pages")
        
        for blog_post in blog_posts:
            template = self.env.get_template('blog/_blog.html')
            try:
                blog_file_name = blog_post["html_file"]
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
                    css_style_sheets = self.css_style_sheets + ['blog.css'],
                    index_ref = "../",
                    blog_post = blog_post,
                    blog_file_contents = blog_file_contents
                )
                file.write(html)
    
    def finished(self):
        """ Finished Message """
        print("Finished webpage creation.")

if __name__ == "__main__":
    SiteGenerator()