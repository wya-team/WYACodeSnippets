# WYACodeSnippets

## 简介

- WYA-iOS-codesnippets是一个WYA团队日常工作中整理出来的用于Xcode的iOS通用代码片段集，其中包含若干专用于WYAOCKit框架的代码片段。

- 整理这个代码片段集的意义有以下几点：

    - 提升开发效率，省掉一些重复性的代码编写，一键生成。

    - 一些常用的写法本身语法或者词语过长比较复杂，难以记忆，例如实现一个类的单利、使用runtime来重写系统空间的方法、block在不同地方的语法不同等

    - 我们在重写一些系统父类方法时候，Xcode是不会自动帮你调用super，有时候我们也会忘记，导致出现一个很难排查的诡异的bug

- 其中以`WYA_`前缀开头的文件是通用的Code Snippets,以`WYAOCKit_`前缀开头的文件是专用于`WYAOCKit`框架的代码片段。在下方的快捷键汇总里，WYAOCKit的代码片段将会以WYAOCKit的形式标记出来。

 
---

## 使用方式

- Xcode的codesnippets文件存放于`~/Library/Developer/Xcode/UserData/CodeSnippets`目录，只要直接把`*.codesnippets`文件放到这个目录下（若没有自己创建）,<font color="red">重启Xcode即可生效。</font>

- 为了方便更新，建议直接将WYACodeSnippets clone到`~/Library/Developer/Xcode/UserData/CodeSnippets`这个目录内：
#### 终端导入

- 执行以下命令

>进入到`~/Library/Developer/Xcode/UserData/CodeSnippets`路径后
>clone WYACodeSnippets文件
>进入到WYACodeSnippets文件路径下
>执行Python脚本
>重启Xcode 

- 命令如下

```
$ cd ~/Library/Developer/Xcode/UserData/CodeSnippets
$ git clone https://github.com/wya-team/WYACodeSnippets.git
$ cd WYACodeSnippets
$ python setup_snippets.py
```

- 当仓库提交新功能后，可以拉取更新，然后进入WYACodeSnippets中执行python脚本即可，不要忘了重启Xcode

<font color="red">注意：
如果使用SourcesTree clone项目时，需要创建的文件夹名字必须使用WYACodeSnippets，否则无法自动导入代码块
</font>


#### 手动导入

- 手动下载后将WYACodeSnippets文件里的<font color="red">`.codesnippet`</font>手动全部拖进<font color="red">`~/Library/Developer/Xcode/UserData/CodeSnippets`</font>路径里

- <font color="red">切记导入完成后需要重新启动Xcode,后续git仓库更新还需要手动导入更新的内容。</font>

---

## 快捷键汇总

#### NSObject

> 1. `pa` - 定义一个assign 的property
> 2. `pw` - 定义一个 weak 的property
> 3. `pc` - 定义一个 copy 的 property
> 4. `ps` - 定义一个 strong 的property
> 5. `psr` - 定义一个 strong, readonly 的property
> 6. `par` - 定义一个 assign, readonly 的 property
> 7. `pwr` - 定义一个 weak, readonly 的property
> 8. `pwd` - 定义一个weak,delegate的property 
> 9. `sharedInstance` 为当前类创建一个实例的单例功能的shareInstance方法

---

#### Block

> 1. `blockArguments` - 声明一个用于方法参数的block
> 2. `blockproperty` - 声明一个用于property的block
> 3. `blocktypedef` - 声明`typedef`定义一个block
> 4. `blockvar` - 定义一个作为局部变量的block

---

#### Method & Function

> 1. `fnv` - 定义一个返回值为void的方法
> 2. `fnv:` - 定义一个返回值为void且带参数的方法
> 3. `fnblock` - 定义一个返回值类型为block的方法
> 4. `fnv_handleEvent` - 定义一个用于UIControl事件回调的方法
> 5. `fnv_longPress` - 定义一个用于`UILongPressGestureRecognizer`的方法回调
> 6. `fnv_pan` - 定义一个用于 `UIPanGestureRecognizer` 的回调方法
> 7. `fnv_tap` - 定义一个用于 `UITapGestureRecognizer` 的回调方法
 
 ---
  
#### UIView

> 1. `getWidth` - 展开`CGRectGetWidth()`
> 2. `getHeight` - 展开 `CGRectGetHeight()`
> 3. `getMinX` - 展开 `CGRectGetMinX()`
> 4. `getMinY` - 展开 `CGRectGetMinY()`
> 5. `getMaxX` - 展开 `CGRectGetMaxX()`
> 6. `getMaxY` - 展开 `CGRectGetMaxY()`
> 7. `addtarget` - 调用 `UIControl addTarget:action:forEvents:` 方法
> 8. `layoutSubviews` - 展开 `layoutSubviews` 方法
> 9. `create_btn` - 创建一个UIButton
> 10. `create_imgview` - 创建一个UIImageView
> 11. `create_keyWindow` - 快速创建keyWindow
> 12. `create_label` - 创建一个UILabel
> 13. `create_tf` - 创建一个UITextField
> 14. `create_view` - 创建一个UIView
> 15. `create_tableView` - 创建一个tableView
> 16. `create_collectionview` - 创建一个collectionview 
> 17. `layer_radius` - 对view设置圆角
> 18. `lay_bordercolor` - 对view设置边框色

---

####  UITableView

> 1.  `initWithStyle` - 展开 `initWithStyle:` 方法
> 2. `initWithStyleForCell` - 展开 `UITableViewCell initWithStyle:reuseIdentifier:` 方法
> 3. `tableViewDelegate` - 展开常用的几个 `UITableViewDelegate` 方法
> 4. `numberOfSectionsInTableView` - 展开 `numberOfSectionsInTableView:`方法
> 5. `numberOfRowsInSection` - 展开 `tableView:numberOfRowsInSection:` 方法
> 6. `cellForRowAtIndexPath` - 展开 `tableView:cellForRowAtIndexPath:` 方法
> 7. `heightForRowAtIndexPath` - 展开 `tableView:heightForRowAtIndexPath:` 方法
> 8. `didSelectRowAtIndexPath` - 展开 `tableView:didSelectRowAtIndexPath:` 方法

---

#### UICollectionView

> 1. `collectionViewDelegate` - 展开常用的几个`UICollectionViewDelegate` 方法
> 2. `numberOfSectionsInCollectionView` - 展开 `numberOfSectionsInCollectionView:`
> 3. `numberOfItemsInSection` - 展开 `collectionView:numberOfItemsInSection:`
> 4. `cellForItemAtIndexPath` - 展开 `collectionView:cellForItemAtIndexPath:`
> 5. `sizeForItemAtIndexPath` - 展开 `collectionView:layout:sizeForItemAtIndexPath:` 方法
> 6. `didSelectItemAtIndexPath` - 展开 `collectionView:didSelectItemAtIndexPath:` 方法
> 7. `didDeselectItemAtIndexPath` - 展开 `collectionView:didDeselectItemAtIndexPath:` 方法

---

#### UIViewController

> 1. `loadView` - 展开 `loadView` 方法
> 2. `viewDidLoad` - 展开 `viewDidLoad` 方法
> 3. `viewWillAppear` - 展开 `viewWillAppear:` 方法
> 4. `viewDidAppear` - 展开 `viewDidAppear:` 方法
> 5. `viewWillDisappear` - 展开 `viewWillDisappear:` 方法
> 6. `viewDidDisappear` - 展开 `viewDidDisappear: `方法
> 7. `viewDidLayoutSubviews` - 展开 `viewDidLayoutSubviews: `方法
> 8. `updateViewConstraints` - 展开 `updateViewConstraints: `方法
> 9. `addChildViewController` - 在当前 UIViewController 里添加 childViewController
> 10. `removeFromParentViewController` - 将 childViewController 从当前的 UIViewController 里移除
 
 ---
 
#### Other

> 1. `pragmalifeCircle` - 展开一个用于Xcode导航的`#pragma mark ======= LifeCircle` Class的系统方法放在最前面
> 2. `pragmaevent` - 展开一个用于Xcode导航的`#pragma mark ======= Event` Class自定义的事件
> 3. `pragmanotifation` - 展开一个用于Xcode导航的`#pragma mark ======= Notifation`Class接收通知的方法
> 4. `pragmalazy` - 展开一个用于Xcode导航的`#pragma mark ======= Lazy`Class懒加载
> 5. `pragmasetter` - 展开一个用于Xcode导航的`#pragma mark ======= Setter`Class的setter方法
> 6. `pragmadelegate` - 展开一个用于Xcode导航的`#pragma mark ======= Delegate`Class遵守的代理
> 7. `pragmanetwork`  - 展开一个用于Xcode导航的`#pragma mark ======= Network`Class的网络请求方法
> 8. `pragmapublic` - 展开一个用于Xcode导航的`#pragma mark ======= Public Method`Class的公有方法
> 9. `pragmaprivate` - 展开一个用于Xcode导航的`#pragma mark ======= Private Method`Class的私有方法
> 10. `pragma` - 展开一个用于Xcode导航的`#pragma mark ======= XXXX` 

## WYAOCKit-CodeSnippets

> 1. `wya_create_sharedview `分享
> 2. `wya_create_segment` 创建WYASegmentControl
> 3. `wya_create_searchBar` 创建搜索框
> 4. `wya_create_popwindow` 创建UIPopoverPresentationController
> 5. `wya_create_keynumberboard_default` 创建数字键盘
> 6. `wya_create_keynumberboard_random` 创建随机数字键盘
> 7. `wya_create_bannerview_local` 加载本地图片的轮播图
> 8. `wya_create_bannerview_url` 加载网络图片的轮播图
> 9. `wya_create_noticebar` 创建通知栏视图
> 10. `wya_create_imagecode` 生成二维码
> 11. `wya_create_progressview` 创建进度条试图
> 12. `wya_alert_surebtn_default`  只有一个按钮弹框
> 13. `wya_alert_default` 默认弹框 
> 14. `wya_alert_textfiled` 有输入框的弹框
> 15. `wya_toast_center` 中心提示
> 16. `wya_toast_bottom` 底部提示
> 17. `wya_toast_success` 成功提示
> 18. `wya_toast_fail` 失败提示
> 19. `wya_toast_netfail` 网络失败
> 20. `wya_toast_loading` 加载
> 21. `wya_segmentedcontrol_delegate` 生成WYASegmentControlDelegate
> 22. `WYA_shareviewdelegate` 分享试图的按钮点击事件代理方法


