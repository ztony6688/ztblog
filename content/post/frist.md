---
title: "Frist"
date: 2023-07-07T08:54:19+08:00
draft: false

---



# hugo + github + labsworld.net
## brew 快速安装 hugo
- brew install hugo
- hugo new site mysite
```
Congratulations! Your new Hugo site is created in /Users/hn_crypto/Desktop/working/mysite.

Just a few more steps and you're ready to go:

1. Download a theme into the same-named folder.
   Choose a theme from https://themes.gohugo.io/ or
   create your own with the "hugo new theme <THEMENAME>" command.
   下载一个新的模板
2. Perhaps you want to add some content. You can add single files
   with "hugo new <SECTIONNAME>/<FILENAME>.<FORMAT>".
3. Start the built-in live server via "hugo server".

Visit https://gohugo.io/ for quickstart guide and full documentation.
```
- 

## 建立新站了解项目目录
```
.
├── archetypes
│   └── default.md
├── assets
├── content
├── data
├── hugo.toml
├── layouts
├── static
└── themes
网站目录结构
```
![](getting.png)
![](create-new-site.png)
![](创建新的模板.png)
```bash
├── archetypes
│   └── default.md
├── assets
├── content
├── data
├── hugo.toml
├── layouts
├── resources
│   └── _gen
│       ├── assets
│       └── images
├── static
└── themes
    └── temp
        ├── LICENSE
        ├── archetypes
        │   └── default.md
        ├── hugo.toml
        ├── layouts
        │   ├── 404.html
        │   ├── _default
        │   │   ├── baseof.html
        │   │   ├── list.html
        │   │   └── single.html
        │   ├── index.html
        │   └── partials
        │       ├── footer.html
        │       ├── head.html
        │       └── header.html
        ├── static
        │   ├── css
        │   └── js
        └── theme.toml

20 directories, 14 files
```
![](介绍%20archetype%20文件夹.png)
![](介绍内容生成.png)
![](data文件夹介绍.png)
![](layouts文件夹介绍.png)
![](layouts-baseof.html介绍.png)
[getbootstrap5.0](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
![](partials模板模块.png)
![](index-sinle-list等页面介绍.png)
![](同上.png)
![](static介绍静态化.png)
## python 批量生成 markdown 内容
### 谷歌head标签介绍
- [og富媒体介绍](https://www.cnblogs.com/cangqinglang/p/8656265.html)


## hugo的标签
### archetypes
- title
- date
- draft 
  1. true
  2. false
  3. 为真时则生成实际文件,否则是调试模式
- tags ['','',''.....]
- categories ['']
- autor: xxx

### 全局网站配置文件
- baseURL = 网站域名
- languageCode = 声明网站的语言
- title
- theme = 使用的模板
- [taxonomies]  新增程序默认以外的网站目录
  * tag = "tags"
  * category = "categories"
  * mood = "moods"
  * ......

### hugo模版的调用标签及知识点
- {{ .Title }}
- {{ .Date }}
- {{.Permalink}} = 调用URL
- {{ .Content }} = 调用md内容
- 自定义变量
   ```
   自定义变量可以编辑在文章模板的 md 文件和 html 模板里
   md 调用样式 : 赋值后  调用>>  {{ .Params.变量名 }}
      使用 Params 方法调用系统默认变量则不需要区分大小写
   html : 赋值  >>{{ $变量名 := 变量 }}  调用>>  {{ $变量名 }}
   ```
- 一部分范围的网页随机展示
   ```
   {{ range .pages }}
      {{ .Title }} {{ .URL }}
   {{ end }}
   这部分代码可以用来实现列表循环或者作用于网站导航栏
   ```

- {{ partial "header" }}
- {{ partial "footer" }}
  ```
   partial 是用来调用模块组件的命令,模块组件放置在 layouts>partials
  ```
- 如果 layouts 下存在与网站目录相同的文件夹那么 hugo 则优先选取 layouts 存在的文件当模板
- "baseof.html"
   ```bash
   这个文件相比于 list.html 和 single.html 权限更高
   baseof.html里存在的内容会应用到网站所有页面
   如果"baseof.html"作用于网站的主体 html 源码,但是其他页面又要有一些差异化,例如网站导航,网站底部,友情链接等等..那么则需要用到以下代码
   在"baseof.html"里将需要差异化的模块用

    {{ block "自定义模块名称" . }}
    模块内容
    {{ end }}
   
   以上代码是将"模块内容"作为可替换的选项

   如果某个页面需要和主体的内容不一样则调用"自定义模块名称"替换

   {{ define "自定义模块名称" }}
   替换后的内容
   {{ end }}

   ```
### hugo 的判断语句和运算符
   - not = 不是或者不等于
   - and
   - or
   - eq = 等于
   - lt = 小于
   - ge = 大于

### hugo 的 json 数据使用方式
   ```
   {{ range .Site.Data.json文件名}}
      {{ .标题 }} <br>
      {{ .作者 }} <br>
      
   {{ end }}
   引用json 文件后以 json 的键值为变量调用数据
   引用区间内包含 html 代码,则可以将整个 html 代码包含在里面再用 json 的数据填充即可
   ```


## hugo模版实例标签代码解读
   - {{ .Site.Language.Lang }} = 在网页头部的语言声明用简短的方式说明网站语言 'en','zh'
   - {{ .Site.Language.LanguageName }} = 在网页头部的语言声明用完整的方式说明网站语言 ' english','china'


## hugo .site 全局配置
   - `postsOnHomePage = 12` #显示在首页的文章数量
   - `tagaOverview = true` #显示全站的 tage 标签,适合专门做一个 tage 集合页面
   - `showProjectsList = true` #显示 Project 列表,需要配合 data 文件夹里的 json 文件输出数据,这个功能可以用来展示 api 的一些数据源,例如某个平台或者行业的最新最火动态,要注意json 的书写格式和缩进格式,不对的话就会报错
   - ```baseURL: http://example.org/  # 网站的基本URL
languageCode: en-us  # 指定网站使用的语言
title: My New Hugo Site  # 网站的首页头部标题
theme: "PaperMod"  # 选择的主题名称

# 用于启用或禁用网站的robots.txt文件生成。如果设置为"true"，Hugo将生成一个robots.txt文件，该文件控制搜索引擎爬虫对网站的访问
enableRobotsTXT: true

# 用于控制是否在构建网站时包含将来发布的内容。如果设置为"false"，Hugo将不会构建将来发布的内容
buildDrafts: false

# 用于控制是否在构建网站时包含将来发布的内容。如果设置为"false"，Hugo将不会构建将来发布的内容
buildFuture: false

# 用于控制是否在构建网站时包含已过期的内容。如果设置为"false"，Hugo将不会构建已过期的内容
buildExpired: false

#用于配置Google Analytics跟踪代码
googleAnalytics: UA-123-45

minify:
  # 用于控制是否对生成的XML文件进行缩小处理。如果设置为"true"，Hugo将禁用对XML文件的缩小处理
  disableXML: true
  # 用于控制是否对生成的输出文件进行缩小处理。如果设置为"true"，Hugo将对输出文件进行缩小处理，以减小文件大小
  minifyOutput: true

# 这是一个参数部分的开始标记，用于定义各种参数和设置
params:
  # 启用谷歌分析、opengraph、twitter-cards 和 schema
  env: production 
  # 网站的标题，将显示在网页标题栏和其他相关位置。在这个例子中，标题被设置为"ExampleSite"
  title: 这是我学习hugo的网站
  # 网站的简介
  description: "这是我学习hugo的网站-description"
  # 网站的关键字
  keywords: [Blog, Portfolio, PaperMod]
  # 网站的作者
  author: Jessica
  # 这是用于OpenGraph和Twitter卡片的图像链接或路径
  images: ["<link or path of image for opengraph, twitter-cards>"]
  # 用于指定日期格式的参数
  DateFormat: "January 2, 2006"
  # 用于指定默认的主题设置（dark, light）
  defaultTheme: auto 
  # 用于控制是否禁用主题切换功能。如果设置为"false"，用户可以在网站上切换不同的主题。如果设置为"true"，则禁用主题切换功能
  disableThemeToggle: false
  # 用于控制是否在文章中显示预计阅读时间。如果设置为 true，则会在文章中显示预计阅读时间
  ShowReadingTime: true
  # 显示分享按钮，使读者可以方便地分享文章到不同的社交媒体平台。如果设置为 true，则会在文章中显示分享按钮
  ShowShareButtons: true
  # 用于控制是否显示文章导航链接，指的就是文章页底部上下页的功能。如果设置为 true，则会在文章中显示导航链接
  ShowPostNavLinks: true
  # 显示面包屑导航，用于显示当前页面在网站结构中的位置。如果设置为 true，则会在页面中显示面包屑导航
  ShowBreadCrumbs: true
  # 控制是否显示代码复制按钮，允许读者方便地复制代码片段。如果设置为 false，则不会在代码块中显示复制按钮
  ShowCodeCopyButtons: true
  # 用于控制是否在文章中显示字数统计。如果设置为 true，则会在文章中显示字数统计
  ShowWordCount: false
  # 用于控制是否在区块和分类/标签列表中显示 RSS 订阅按钮。如果设置为 true，则会在区块和分类/标签列表中显示 RSS 订阅按钮
  ShowRssButtonInSectionTermList: true
  # 用于控制是否使用 Hugo 自动生成的目录（TOC）
  UseHugoToc: true
  # 用于控制是否禁用特殊样式的第一篇文章。如果设置为 false，则不会禁用特殊样式的第一篇文章
  disableSpecial1stPost: false
  # 用于控制是否禁用滚动到页面顶部的功能。如果设置为 false，则不会禁用滚动到页面顶部的功能
  disableScrollToTop: false
  # 用于控制是否在文章中启用评论功能。如果设置为 false，则不会在文章中启用评论功能
  comments: true
  # 用于控制是否隐藏文章的元数据信息，如作者、日期等。如果设置为 false，则不会隐藏元数据信息
  hidemeta: false
  # 用于控制是否隐藏文章的摘要。如果设置为 false，则不会隐藏文章摘要
  hideSummary: false
  # 用于控制是否显示文章的目录（TOC）。如果设置为 false，则不会显示文章目录
  showtoc: true
  # 用于控制文章目录是否默认展开。如果设置为 false，则不会默认展开文章目录
  tocopen: true

  # 包含网站资源相关设置的部分
  assets:
    # 用于禁用 highlight.js（代码高亮库）。如果取消注释并将其设置为 true，则会禁用 highlight.js
    disableHLJS: false 
    ## disableFingerprinting: true
    # 设置网站的 favicon（网站图标）设置16/32像素（favicon16x16: "<link / abs url>"）。你需要提供一个链接或绝对路径，指向你的 favicon 图片文件
    favicon: "<link / abs url>"
    # 设置网站的 Apple Touch Icon，即在 iOS 设备上显示的图标
    apple_touch_icon: "<link / abs url>"
    # 设置网站在 Safari 浏览器中的固定标签页图标
    safari_pinned_tab: "<link / abs url>"

  # 标签的设置部分，用于定义标签的属性和样式
  label:
    # 用于设置标签的文本内容
    text: "这是我的学习网站-------"
    # 用于设置标签的图标，即显示在标签上的图像
    icon: /apple-touch-icon.png
    # 设置标签图标的高度
    iconHeight: 35

  # 个人资料模式的设置部分
  profileMode:
    # 用于控制是否启用个人资料模式。如果设置为 false，则禁用个人资料模式（需要明确设置）
    enabled: false
    # 用于设置个人资料模式的标题，即显示在个人资料顶部的文本
    title: ExampleSite
    # 用于设置个人资料模式的副标题
    subtitle: "This is subtitle"
    # 设置个人资料模式的图像
    imageUrl: "<img location>"
    # 设置个人资料模式图像的宽度
    imageWidth: 120
    # 设置个人资料模式图像的高度
    imageHeight: 120
    # 设置个人资料模式图像的标题
    imageTitle: my image

    # 按钮列表的设置部分，用于定义在个人资料模式中显示的按钮
    buttons:
      # 设置按钮的显示文本
      - name: Posts
      # 设置按钮的链接地址
        url: posts
      - name: Tags
      # 另一个按钮的设置，用于显示 "Tags" 按钮并指定相应的链接地址。
        url: tags

  # 设置主页信息参数
  # homeInfoParams:
  #   # 设置主页信息的标题,\U0001F44B 是一个 Unicode 表情符号的表示方式
  #   Title: "Hi there \U0001F44B"
  #   # \U0001F44B 是一个 Unicode 表情符号的表示方式
  #   Content: Welcome to my blog

  # # 定义在网站上显示的社交媒体图标及其链接
  # socialIcons:
  #   - name: twitter
  #     url: "https://twitter.com/"
  #   - name: stackoverflow
  #     url: "https://stackoverflow.com"
  #   - name: github
  #     url: "https://github.com/"
  #   - name: youtube
  #     url: "https://youtube.com/"

  # 分析工具的设置部分
  analytics:
    google:
      SiteVerificationTag: "XYZabc"
    bing:
      SiteVerificationTag: "XYZabc"
    yandex:
      SiteVerificationTag: "XYZabc"

  # 设置封面（cover）的隐藏选项
  cover:
    # 控制封面的隐藏。如果设置为 true，则封面会在网站的其他位置隐藏，但会在结构化数据中保留。换句话说，封面将在结构化数据中可见，但在其他页面上会被隐藏
    hidden: true 
    # 控制封面在列表页面和主页上的隐藏。如果设置为 true，则封面会在列表页面和主页上隐藏
    hiddenInList: true 
    # 控制封面在单个页面上的隐藏。如果设置为 true，则封面会在单个页面上隐藏
    hiddenInSingle: true 

  # 设置编辑文章的选项
  editPost:
    # 设置编辑文章的链接地址。你需要提供一个指向你的文章存储库（repository）中内容文件所在路径的链接。在这个示例中，编辑文章的链接被设置为 GitHub 上的存储库链接，路径使用 <path_to_repo>/content 表示
    URL: "https://github.com/<path_to_repo>/content"
    # 设置编辑文章链接上的文本内容，即显示在编辑链接上的文本。在这个示例中，编辑文章链接的文本被设置为 "Suggest Changes"
    Text: "Suggest Changes" 
    # 编辑链接中附加文件路径。如果设置为 true，则会在编辑链接的末尾添加文件路径信息
    appendFilePath: true 

  # Fuse.js 搜索选项的设置部分
  # https://fusejs.io/api/options.html
  fuseOpts:
    # 设置搜索是否区分大小写。如果设置为 false，则搜索将不区分大小写
    isCaseSensitive: false
    # 控制搜索结果是否应该排序。如果设置为 true，则搜索结果将按照匹配程度进行排序
    shouldSort: true
    # 设置搜索结果中匹配项的位置权重。在这个示例中，位置权重被设置为 0，表示位置对搜索结果的排序没有影响
    location: 0
    # 设置搜索结果中匹配项的距离权重。在这个示例中，距离权重被设置为 1000，表示距离对搜索结果的排序有一定影响，但不是主要因素
    distance: 1000
    # 设置搜索结果匹配的阈值。在这个示例中，阈值被设置为 0.4，表示只有匹配度高于 0.4 的结果会被返回
    threshold: 0.4
    # 设置最小匹配字符长度。在这个示例中，最小匹配字符长度被设置为 0，表示搜索结果中的每个字符都会被考虑匹配
    minMatchCharLength: 0
    # 设置要在搜索中匹配的字段。在这个示例中，搜索将匹配 title、permalink、summary 和 content 字段
    keys: ["title", "permalink", "summary", "content"]

# 设置网站的主菜单
menu:
  main:
    # 设置菜单项的唯一标识符
    - identifier: home
    # 设置菜单项的显示名称
      name: Home
    # 设置菜单项的链接地址
      url: /
    # 设置菜单项的权重，用于控制菜单项在菜单中的排序位置
      weight: 10
    - identifier: posts
      name: Blog
      url: /posts/
      weight: 20
    - identifier: contents
      name: Contents
      url: https://example.org
      weight: 30

outputs:
    home:
        - HTML
        - RSS
        - JSON # is necessary
# Read: https://github.com/adityatelange/hugo-PaperMod/wiki/FAQs#using-hugos-syntax-highlighter-chroma
# 控制是否使用类名来标记代码高亮
pygmentsUseClasses: true
# 标记语言（markup）设置部分
markup:
  highlight:
    # 控制是否为代码块添加类名。如果设置为 false，则会为代码块添加类名，以实现代码高亮样式
    noClasses: false
    # 设置是否为行号添加锚点。如果取消注释并将其设置为 true，则会为每行行号添加一个锚点
    # anchorLineNos: true
    # 设置是否使用 Markdown 的代码围栏语法。如果取消注释并将其设置为 true，则会使用 Markdown 的代码围栏语法来标记代码块
    # codeFences: true
    # 设置是否自动猜测代码的语法。如果取消注释并将其设置为 true，则会尝试自动猜测代码的语法
    # guessSyntax: true
    # 设置是否显示行号。如果取消注释并将其设置为 true，则会在代码块中显示行号
    # lineNos: true
    # 设置代码高亮的样式。你可以根据需要取消注释并设置适当的样式，比如 "monokai"
    # style: monokai


    baseURL: http://example.org/
languageCode: zh-cn # en-us
title: 我的博客
keywords: [Blog]
description: "这是一个纯粹的博客......" #启动首页简介
author: Sulv
theme: PaperMod
googleAnalytics: UA-123-45 # 谷歌统计
Copyright: Sulvsss #网站品牌

menu:
  main:
    - identifier: search
      name: 🔍搜索
      url: search
      weight: 1
    - identifier: home
      name: 🏠主页
      url: /
      weight: 2
    - identifier: posts
      name: 📚文章
      url: posts
      weight: 3
    - identifier: archives
      name: ⏱时间轴
      url: archives/
      weight: 20
    - identifier: tags
      name: 🔖标签
      url: tags
      weight: 40
    - identifier: about
      name: 🙋🏻‍♂️关于
      url: about
      weight: 50
    - identifier: links
      name: 🤝友链
      url: links
      weight: 60

outputs:
    home:
        - HTML
        - RSS
        - JSON

socialIcons:
    - name: github
      url: "https://github.com/xyming108"
    - name: twitter
      url:  "img/twitter.png"
    - name: facebook
      url: "https://www.facebook.com/profile.php?id=100027782410997"
    - name: instagram
      url: "img/instagram.png"
    - name: QQ
      url: "img/qq.png"
    - name: WeChat
      url: "img/wechat.png"
    - name: email
      url: "mailto:1931559710@qq.com"
    - name: RSS
      url: "index.xml"

assets:
    favicon: "img/Q.gif"
    favicon16x16: "img/Q.gif"
    favicon32x32: "img/Q.gif"
    apple_touch_icon: "Q.gif"
    safari_pinned_tab: "Q.gif"


minify:
    disableXML: true 
    #minifyOutput: true #启用 html 代码压缩

#permalinks: #设置网站链接显示方式
  #post: "/:title/"
  #post: "/:year/:month/:day/:title/"


paginate: 15    # 每页显示的文章数
enableInlineShortcodes: true #允许内联短码
enableEmoji: true # 允许使用 Emoji 表情，建议 true
enableRobotsTXT: true # 允许爬虫抓取到搜索引擎，建议 true
hasCJKLanguage: true # 自动检测是否包含 中文日文韩文 如果文章中使用了很多中文引号的话可以开启
buildDrafts: false
buildFuture: false
buildExpired: false
defaultContentLanguage: en # 最顶部首先展示的语言页面
defaultContentLanguageInSubdir: true
params:
    env: production # 打开 HEAD 富媒体展示
    #author: ["Me", "You"] # multiple authors
    defaultTheme: auto  # defaultTheme: light or  dark 
    disableThemeToggle: false
    DateFormat: "2006-01-02" #时间展示样式
    ShowShareButtons: true #显示分享组件
    ShowReadingTime: true #显示阅读时间
    disableSpecialistPost: true
    displayFullLangName: true
    ShowPostNavLinks: true #显示上一页下一页
    ShowBreadCrumbs: true #显示面包屑导航
    ShowCodeCopyButtons: true #代码块显示复制功能
    hideFooter: false # 隐藏页脚
    ShowWordCounts: true #显示文章字数
    VisitCount: true #显示访问次数
    ShowAllPagesInArchive: true # 归档页面设置需要
    ShowLastMod: true #显示文章最后更新时间
    ShowRssButtonInSectionTermList: true  #显示 rss 订阅组件
    ShowFullTextinRSS: true # rss 配置
    ShowToc: true # 显示文章栏目
    TocOpen: false # 自动展开文章栏目
    disableScrollToTop: false #置顶或者是阅读排行
    #comments: true
#     # editPost:
#     #     URL: "https://github.com/adityatelange/hugo-PaperMod/tree/exampleSite/content"
#     #     Text: "Suggest Changes" # edit text
#     #     appendFilePath: true # to append file path to Edit link
#     label:
#       text: "Sulv's Blog"
#       #icon: "img/Q.gif"
#       icon: "https://www.sulvblog.cn/Q.gif"
#       iconHeight: 35

cover:
    hidden: true # hide everywhere but not in structured data
    hiddenInList: true # hide on list pages and home
    hiddenInSingle: true # hide on single page

fuseOpts:
    isCaseSensitive: false
    shouldSort: true
    location: 0
    distance: 1000
    threshold: 1
    minMatchCharLength: 0
    keys: ["title", "permalink", "summary", "content"]

# twikoo:
#   version: 1.4.11

taxonomies:
    category: categories
    tag: tags
    series: series

markup:
    goldmark:
        renderer:
            unsafe: true # HUGO 默认转义 Markdown 文件中的 HTML 代码，如需开启的话
    highlight:
        # anchorLineNos: true
        codeFences: true  
        guessSyntax: true
        lineNos: true
        # noClasses: false
        # style: monokai
        style: darcula

        # codeFences：代码围栏功能，这个功能一般都要设为 true 的，不然很难看，就是干巴巴的-代码文字，没有颜色。
        # guessSyntax：猜测语法，这个功能建议设置为 true, 如果你没有设置要显示的语言则会自动匹配。
        # hl_Lines：高亮的行号，一般这个不设置，因为每个代码块我们可能希望让高亮的地方不一样。
        # lineNoStart：行号从编号几开始，一般从 1 开始。
        # lineNos：是否显示行号，我比较喜欢显示，所以我设置的为 true.
        # lineNumbersInTable：使用表来格式化行号和代码,而不是 标签。这个属性一般设置为 true.
        # noClasses：使用 class 标签，而不是内嵌的内联样式

privacy:
    vimeo:
        disabled: false
        simple: true

    twitter:
        disabled: false
        enableDNT: true
        simple: true

    instagram:
        disabled: false
        simple: true

    youtube:
        disabled: false
        privacyEnhanced: true

services:
    instagram:
        disableInlineCSS: true
    twitter:
        disableInlineCSS: true
        
```