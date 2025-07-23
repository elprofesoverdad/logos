
Virtua Creative Technology
Blog

  
Markdown Tips & Tricks - Thinking Outside the Box
Part 1 - Adding elements & applying classes onto markdown files.

October 15th, 2015   By Marcia Ramos
Markdown Tips & Tricks - Thinking Outside the Box
Markdown
For those who are used to write in Markdown or are beginning to learn this language, we are here to provide you some tricks and tips that may help you to think outside the box and make some :zap: “magic” :zap: when writing your files.

Markdown Tips & Tricks - Part 1
On this article, you will learn how to add new HTML elements (also div tags) and how to apply classes to html elements onto your markdown files.

Markdown Tips & Tricks - Part 2
On the next post, we are going to show you how to embed videos on your markdown files. This second part will be published at October 26th.

Additional Information
For markdown basics, you can check this GitHub article, which provides us with a bunch of very often applied markup.

All the examples given below were tested on our Blog written in Jekyll, hosted by GitHub Pages, within a gh-pages branch for a project website. Depending on your server or on the way your site is build, some of these tips might not work. Anyway, feel free to give them a try, even if your markdown files don’t have the same configuration or compilation.

Settings
Our Jekyll _config.yml settings are the following:

---
# your settings ...

highlighter: rouge
markdown: kramdown
kramdown:
  input: GFM          # this is a support for GitHub Flavored Markdown

gems:
  - jemoji            # this is a support for emoticons
  - jekyll-mentions   # this is a support for GitHub user's mentions by adding @ before their names

# your settings ...
---
The tips provided by this post worked very well using Kramdown with GFM and Rouge. It works fine when replacing rouge for pygments too. Other markdown and highlighters haven’t been tested yet, but you are more than invited to give it a try and tell us if works or not! :smiley:

Our build has been made by running bundle exec jekyll serve --safe on the command prompt, at the local root folder, as recommended by GitHub. Using the --safe mode allows you to build your site locally in the closest way that GitHub will do it, avoiding building errors when uploading your files to GitHub.

Update!

It seems to have a bug on GitHub Pages regarding the --safe flag! So, for now, we recommend you to serve Jekyll with Bundler without this flag, at least until they fix it. Run bundle exec jekyll serve and watch for changes running bundle exec jekyll serve --watch.

Our default.html file (where the markdown posts are called to) is placed at our _includes folder and is a HTML5 document. Our styles are written in CSS3.

Adding HTML Elements
Let’s begin with new elements. Did you know you can add HTML elements to your markdown? For example, if you need a horizontal line, you can add it as the code below:

1
2
3
4
5
 Some text here
// blank line
<hr>
// blank line
Something else here 
…and will be compiled to…

<p>Some text here</p>
<hr>
<p>Something else here</p>
Note that we left the lines 2 and 4 empty, this is a condition for html elements to be untouched when your markdown is compiled.

Now you can freely style your <hr> in your CSS.

Just to let you know, in this particular case you can use just a sequence of ----- onto your markdown and it will produce a <hr> tag when compiled to html. But sometimes you can’t run from using some html tags themselves in order to have the results you want.

Feel free to use the tag `` the same way for breaking lines.

  Don't forget to leave a blank line between some regular markdown text and a html tag, otherwise you might face errors during files compilation!

Custom Elements
Following the same logic, HTML 5 allows you to add some extra elements, and you are also free to make up your own. We have added a few custom elements to this blog. For example, as you might have noticed, some of our titles on this blog are blue. How did we do that?

This is not a <span> tag. Actually, we made a new element up, called <mkp-blue>. You can call elements whatever you want. This element has only one propriety defined in our CSS, all the others are inherit from its parent element:

mkp-blue {
	color: blue;
}
We can use these new elements combined with markup, for example, this line:

Hello! I'm a **<mkp-blue>blue</mkp-blue>** word in a regular markdown text!
…will be compiled to:

<p>Hello! I'm a <strong><mkp-blue>blue</mkp-blue></strong> word in a regular markdown text!</p>
…and this is going to be the result displayed on users’ browsers:

Hello! I'm a blue word in a regular markdown text!

BUT, you can’t do the opposite, using a markup within an html tag, like:

Hello! I'm a <mkp-blue>**blue**</mkp-blue> word in a regular markdown text!
… as it will be compiled to:

<p>Hello! I'm a <mkp-blue>**blue**</mkp-blue> word in a regular markdown text!</p>
… and will produce this result:

Hello! I'm a **blue** word in a regular markdown text!

… which probably is not what you want.

Workaround
The good news is, with Kramdown you can do that by adding this markup before the section you want to combine HTML and markdown markup:

{::options parse_block_html="true" /}
It will allow you to do crazy stuff like:

{::options parse_block_html="true" /}

<p class="bkgblue">Hello! This is gonna be **bold**! And this, <span class="color_blue">**blod and blue**</span>!</p>
… which will produce:

Hello! This is gonna be bold! And this, blod and blue!

Then, if you need, you can close the HTML/Markdown block parser with:

{::options parse_block_html="false" /}
That’s it, you can add as many default or non-default elements to your markdown file, as long as you leave blank lines above and below them.

Attention!
Making up your own custom elements is not recommended when you want to stick to the standards. Also, they haven’t cross-browser compatibility. There is an article where the author goes deep into this subject. The minimum recommendation is adding this code to the site <head> when you use them:

<!--[if lt IE 9]> 
<script> document.createElement("element_name"); </script>
<![endif]-->
This will create a new element when the http request to your site is comming from Internet Explorer 9.

Adding HTML Divs
Exactly as we just have done, you can add some html divs to your markdown. And with divs, you can do pretty much anything you like, such as giving classes, ids, transitions, and anything that a regular <div> tag supports in HTML 5.

For example, let’s say you want a particular image style at some point, you can just wrap it into a <div> and that’s it!

...

<div class="example">
  <img src="http:something.com/img/img1.png" alt="Some alternative text">
</div>

...
The result will be exactly as expected:

...
<div class="example">
  <img src="http:something.com/img/img1.png" alt="Some alternative text">
</div>
...
And you customize your special image as you want, for example:

.example img {
	width: 30%;	
	border: 1px solid #333;	
	box-shadow: 2px 2px 5px #999;
	border-radius: 5px;
}
Here is the result:

Some alternative text
Of course we could have styled the image itself in this case, but sometimes we need nested elements in order to produce the results we want. A very common case is giving an element a position="relative" and its nested element a position="absolute". We cannot achieve the same results by playing around just with one of them, we’ll need them both!

Applying HTML Classes
When I first started writing in markdown, I googled something like “how to apply classes to markdown” and couldn’t find much. BUT, when I tried something unusual, for my best surprise, it worked!

For example, let’s say you want to apply a different class to a paragraph. Instead of writing the regular text on markdown, as:

...
Hello! I'm a regular textile paragraph written in a markdown file!
...
… you are free to write it as a <p>...</p> HTML tag, like:

1
2
3
4
5
...

<p class="myclass">Hello! I'm a regular HTML paragraph written in a markdown file!</p>

...
… and it will be compiled to:

...
<p class="myclass">Hello! I'm a regular HTML paragraph written in a markdown file!</p>
...
… and will be displayed on the browser like:

Hello! I'm a regular HTML paragraph written in a markdown file!

The only difference is that we have applied a new class to the paragraph, giving it a bluish background. But you can style your tags according to your needs!

That’s it! As simple as it looks! This way you are free to style your HTML tags compiled from your markdown files however you want!

Just do not forget to always leave a blank line between your markdown regular text and any HTML tag!

Update!
I’ve just found out an easy way to applying classes to your markdown markup with Kramdown!! Look at that:

I’m in a green box now!

This was simply achieved by this piece of code:

I'm in a green box now!
{: .bkggreen}
It’s awesome, isn’t it?! :dancers:

What if I need more than one .class?

I have tree classes now!
{: .class1 .class2 .class3}
What if I need an id?

# I have an ID now! => works for headings too!
{: #i_am_an_id}
What if I need both, an id and a .class?

I have an ID and a CLASS now!
{: #i_am_an_id .class}
What if I need to add a .class to an image?

![ALT text](path/to/img/image.png){: .class}
I just loved this! Check the full reference out!

Done!
All right then, now that you know that you can add html elements and apply classes to them in markdown files, it’s time to make it work for you! Go on and use them freely, you’ll see that the results are fantastic and at the same time we keep the astonishing advantages of writing in markdown!

Don’t lose our next post, where we will show you how to embed videos in markdown files. It can be a little tricky, specially giving them responsiveness, but we are here to share our knowledge with you! :smiley:

That's all folks!
We hope to have been helpful! Please, if you enjoyed this article, share it, recommend it or leave a comment to let us know!

If you have any questions or suggestions, please feel free to get in touch with us by filling our contact form.

Thanks for reading! Check our next article Markdown Tips and Tricks - Part 2!

Stay tuned! Follow us on Twitter, Google+ or subscribe to our YouTube Channel!

Related Article(s)
⇢ How to publish your website on GitHub
⇢ How to publish Project Websites on GitHub
References
☆ GitHub
☆ GitHub Pages
☆ Jekyll
☆ GitHub Flavored Markdown
☆ Jekyll Documentation
☆ Markdown
☆ Kramdown
Image Credits
★ Art work: Virtua Creative
★ Illustrations: we have downloaded from Freepik the original box and the original bulb.
Last update: 04/10/2016 - 19:32h.
 jekyll (5) , github (7) , tutorials in English (5)
 markdown (5) , kramdown (4) , jekyll (7) , github (7) , github pages (5) , git (7)
← Previous  TopNext →
Share
  Virtua Creative
Virtua Creative Technology


© 2016 Virtua Creative. Virtua Creative Technology by RamosMD. All rights reserved.
Template only under MIT License: download it here. Brands are here exposed for illustration purposes only.