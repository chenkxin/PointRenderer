# mitsuba 一些说明

我在`mitsuba 安装` 文件中记录了一些一开始安装使用 `mitsuba` 时碰到的部分问题。

## mitsuba 版本问题

注意， 要区分 `mitsuba` 的版本，因为不同版本的 `mitsuba`，其对应的 `xml` 文件的配置有些许不同，具体可以查看官网文档。

比如 `mitsuba 0.6` 到 `mitsuba 2` 版本，`ldrfilm` 改成了 `hdrfilm` ，然后很多属性部分， 由驼峰法改成下划线形式表示， 如 `maxDepth` 变成 `max_depth`.

其他修改处不再赘述，具体可以查阅官网文档。

我在提供的 `point_colorful_seg.py` 文件中，有写两个版本的 `xml` 文件，包括对应的文件头文件尾文件体，如果需要可以有选择性的注释掉相关代码，同时不要忘记在渲染的时候调用对应版本的 `mitsuba`。

可以使用 `mitsuba --version` 查看默认版本。

注意，如果 `mitsuba` 版本和 `xml` 文件的版本不匹配的话，会报错的。



不同版本也有不同版本的优缺点，比如 `mitsuba 2` 版本可以渲染得到更加清晰的 `exr` 文件，而且支持 `gpu` 渲染等。

当然，如果对画质要求没有那么极端， `mitsuba 0.6` 也是够用的。

注意，分辨率可以在文件头里调。

![image-20230513015014531](mitsuba%20%E4%B8%80%E4%BA%9B%E8%AF%B4%E6%98%8E.assets/image-20230513015014531.png)

## gpu 渲染

`mitsuba` 也有很多种渲染模式，比如 `scalar_rgb, scalar_spectral, packet_rgb, packet_spectral, gpu_rgb, gpu_spectral` 等。

理论上，使用 `gpu` 渲染的速度会快很多，`mitsuba 2` 支持 `gpu` 渲染模式。

但是，似乎使用 `gpu` 渲染会非常占用显存， 我在实验过程中， 尝试使用 `gpu` 进行渲染， 必须要把采样点降到极低，降低到了4，这样渲染的效果很差，很粗糙。

因此，不建议使用 `gpu` 渲染。

