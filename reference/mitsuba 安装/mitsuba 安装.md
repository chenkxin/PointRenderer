# mitsuba 安装

`mitsuba`可以用来渲染点云。

现在出到 `3.0` 后的版本了。

安装 `mitsuba3`， 直接 `pip install mitsuba`

安装 `mitsuba2`， `github` 下载项目， 按照手册编译。 `git clone --recursive git@github.com:mitsuba-renderer/mitsuba2.git`

[mitsuba2 document](https://mitsuba2.readthedocs.io/en/latest/)

## mitsuba1

### 安装 mitsuba1

`github` 下载， `git clone --recursive git@github.com:mitsuba-renderer/mitsuba.git `

![image-20220810205430531](mitsuba%20%E5%AE%89%E8%A3%85.assets/image-20220810205430531.png)

[document](http://mitsuba-renderer.org/releases/current/documentation.pdf)

### 安装依赖

因为比较久远的版本， 有些依赖在 `20.04` 可能名字都不一样。

```bash
sudo apt-get install build-essential scons mercurial qt4-dev-tools libpng12-dev libjpeg-dev libilmbase-dev libxerces-c-dev libboost-all-dev libopenexr-dev libglewmx-dev libxxf86vm-dev libpcrecpp0 libeigen3-dev libfftw3-dev
```

#### qt4-dev-tools 装不了

[solution](https://askubuntu.com/questions/1274134/cannot-install-qt-4-on-ubuntu-20-04-quite-universal-circuit-simulator-qucs)

```bash
sudo add-apt-repository ppa:rock-core/qt4
sudo apt update

sudo apt install qt4-dev-tools libqt4-dev libqt4-core libqt4-gui
# or
sudo apt install qt4-dev-tools libqt4-dev libqtcore4 libqtgui4
```

#### libpng12-dev 装不了

换成 `libpng-dev`

或者， 添加源： `ppa:linuxuprising/libpng12`

```bash
sudo add-apt-repository ppa:linuxuprising/libpng12
sudo apt update

sudo apt install libpng12-dev
```

[solution](https://www.linuxuprising.com/2018/05/fix-libpng12-0-missing-in-ubuntu-1804.html)

#### libpcrecpp0 装不了

换成 `libpcrecpp0v5`

#### scons

![image-20220810232135100](mitsuba%20%E5%AE%89%E8%A3%85.assets/image-20220810232135100.png)

报没有指定 `config.py`, 直接在配置里面写死 `configFile = "config.py"`



`print 'gdsagfg'`, 没有这种写法， 改成 `print('gdsagfg')`

### 测试

可以了。

![image-20220810233325168](mitsuba%20%E5%AE%89%E8%A3%85.assets/image-20220810233325168.png)

![image-20220810233427666](mitsuba%20%E5%AE%89%E8%A3%85.assets/image-20220810233427666.png)

![image-20220811122718216](mitsuba%20%E5%AE%89%E8%A3%85.assets/image-20220811122718216.png)

## mitsuba2

### 安装 mitsuba2

```bash
sudo apt install -y libz-dev libpng-dev libjpeg-dev libxrandr-dev libxinerama-dev libxcursor-dev
```

这一步的时候， 因为 `mitsuba` 安装的时候， 装了比较老的 `libpng12-dev`， 现在这个包已经升级了， `mitsuba2` 依赖于升级后的 `libpng-dev`， 所以这个包会被重装。

不过重装这个包， 似乎不影响 `mitsuba` 的运行。

![image-20220812195411173](mitsuba%20%E5%AE%89%E8%A3%85.assets/image-20220812195411173.png)

### mitsuba2 gpu 计算

似乎需要额外安装 `Optix7`

![image-20220812220632784](mitsuba%20%E5%AE%89%E8%A3%85.assets/image-20220812220632784.png)

#### 先修改 mitsuba.conf， 再进行编译 mitsuba

![image-20220812221001459](mitsuba%20%E5%AE%89%E8%A3%85.assets/image-20220812221001459.png)

#### 一个注意点， enable 里， 最后一个不能带逗号

![image-20220812221559220](mitsuba%20%E5%AE%89%E8%A3%85.assets/image-20220812221559220.png)

`"gpu_spectral"` 后面不能加逗号了， 否则会报错。 这是一个细节！！！

#### ldrfilm 改成了 hdrfilm

![image-20220812225401741](mitsuba%20%E5%AE%89%E8%A3%85.assets/image-20220812225401741.png)

实际上， `0.6` 的 `xml` 有些编译不了的， 看报错， 对照 `misuba2` 文档的 `example` 修改即可。

其他修改处不再赘述。

大部分都是属性部分， 由驼峰法改成下划线形式表示， 如 `maxDepth` 变成 `max_depth`

#### 安装 optix

下载 `optix7.5`， `bash xxxx.sh`

解压出来文件， 在`SDK`里面有 `INSTALL-LINUX.txt`， 有写编译方式。

自己没有注意看， 还去找安装文档， 找半天找不到， 结果就在文件夹里。

![image-20220812234610827](mitsuba%20%E5%AE%89%E8%A3%85.assets/image-20220812234610827.png)

![image-20220812234740677](mitsuba%20%E5%AE%89%E8%A3%85.assets/image-20220812234740677.png)

`ccmake` 也要安装一下：

```bash
sudo apt-get install cmake-curses-gui
```

`ccmake` 是交互式的 `cmake`， [ccmake 和 cmake 的区别](https://blog.csdn.net/arackethis/article/details/42155589)

##### doxygen not found

![image-20220812235215283](mitsuba%20%E5%AE%89%E8%A3%85.assets/image-20220812235215283.png)

```bash
sudo apt-get install doxygen
```

##### doxygen missing components: dot

似乎是没有 `graphviz`， [github issue](https://github.com/labapart/gattlib/issues/129)

![image-20220813005143886](mitsuba%20%E5%AE%89%E8%A3%85.assets/image-20220813005143886.png)

```bash
sudo apt install graphviz
```

![image-20220813005320941](mitsuba%20%E5%AE%89%E8%A3%85.assets/image-20220813005320941.png)

可以了。

---

##### Reading OpenEXR version

![image-20220812235818246](mitsuba%20%E5%AE%89%E8%A3%85.assets/image-20220812235818246.png)

卡在这里了， 很奇怪。 

```bash
sudo apt install openexr
sudo apt install libopenexr-dev
```

重装也没有用。

![image-20220812235928407](mitsuba%20%E5%AE%89%E8%A3%85.assets/image-20220812235928407.png)

---

既然 `ccmake` 是 `cmake` 的 `gui` 形式， 那么我不需要修改 `cmake` 过程中的相关编译配置的话， 也就没必要使用 `ccmake` 了。

直接 `cmake ..`

![image-20220813001153404](mitsuba%20%E5%AE%89%E8%A3%85.assets/image-20220813001153404.png)

直接 `cmake` 就可以入去 `OpenEXR` 的。

#### ![image-20220813001657788](mitsuba%20%E5%AE%89%E8%A3%85.assets/image-20220813001657788.png)

[`Vulkan`](https://packages.lunarg.com/#) 找不到， 安装一下， [博客](https://blog.csdn.net/arackethis/article/details/42155589)

```bash
wget -qO - https://packages.lunarg.com/lunarg-signing-key-pub.asc | sudo apt-key add -
sudo wget -qO /etc/apt/sources.list.d/lunarg-vulkan-1.3.216-focal.list https://packages.lunarg.com/vulkan/1.3.216/lunarg-vulkan-1.3.216-focal.list
sudo apt update
sudo apt install vulkan-sdk
```

##### Performing Test CMAKE_HAVE_LIBC_PTHREAD - Failed

要仔细看 `cmake` 的日志啊， 还有一些问题的。

![image-20220813002456835](mitsuba%20%E5%AE%89%E8%A3%85.assets/image-20220813002456835.png)

看起来是 `pthreads` 的问题。

安装一下：

```bash
sudo apt-get install libblis64-3-pthread
```

```bash
sudo apt-get install glibc-doc

sudo apt-get install manpages-posix-dev
```

```bash
sudo apt -y install libboost-tools-dev libboost-thread1.62-dev magics++
```

```bash
sudo apt install librdkafka-dev
```

```bash
sudo apt install libc6-amd6
```

![image-20220813011108295](mitsuba%20%E5%AE%89%E8%A3%85.assets/image-20220813011108295.png)

装这个把5个其他包删掉了， 重新装回来， 不然 clang 都没有。

---

实在搞不懂了， `pthread` 又是有的， `cmake` 的 `CMakeLists.txt` 编译链接模块也加了， 各种方法都试过了。

甚至显卡也重装到最新的 `515.65.01` 了。 但是就是没办法动态链接， 编译。

搞到凌晨四点半， 不搞了。

---

##### 到 m4 上重新尝试编译， m4 的环境相对干净

```bash
sudo apt install cmake
```

![image-20220813154319630](mitsuba%20%E5%AE%89%E8%A3%85.assets/image-20220813154319630.png)

这边用的是 `c` 和 `c++`， `m3` 用的是 `clang` 和 `clang++` ， 说明和编译器无关。

除了常见的 `doxygen` 之类的需要安装以外， 还是没有 `pthread`

![image-20220813154453074](mitsuba%20%E5%AE%89%E8%A3%85.assets/image-20220813154453074.png)

老问题。

我怀疑是 `CMakeLists.txt` 的问题。

---

```bash
sudo apt install libblis-pthread-dev
```

还是不行。

![image-20220813155453912](mitsuba%20%E5%AE%89%E8%A3%85.assets/image-20220813155453912.png)

![image-20220813155803188](mitsuba%20%E5%AE%89%E8%A3%85.assets/image-20220813155803188.png)

---

```bash
sudo apt-get install libpthread-stubs0-dev
```

已经安装过了。

---

```bash
sudo apt install manpages-posix
```

也试过了。

---

`pthreads` ubuntu 上安装

![image-20220813162108409](mitsuba%20%E5%AE%89%E8%A3%85.assets/image-20220813162108409.png)

放到 `/lib` 或者 `/lib/x86_64-linux-gnu` 下还是失败。

---

##### undefined reference to `Imf_2_3::FrameBuffer

使用 clang-9 , `make` 只能到 `25%`

![image-20220813180551450](mitsuba%20%E5%AE%89%E8%A3%85.assets/image-20220813180551450.png)

用 `gcc-8 g++-8 gcc-7 g++-7` 还能到 `55%`

![image-20220813180745464](mitsuba%20%E5%AE%89%E8%A3%85.assets/image-20220813180745464.png)

---

感觉不对啊。

![image-20220813183404472](mitsuba%20%E5%AE%89%E8%A3%85.assets/image-20220813183404472.png)

`openexr` 的路径， 怎么是 `/usr/local/mitsuba-2/build/dist/libIlmImf.so`

我去 `/usr/local/mitsuba-2/build/dist/` 把 `libIlmImf.so` 重命名成 `libIlmImf.so.bak`

再 `cmake ..`

![image-20220813184204764](mitsuba%20%E5%AE%89%E8%A3%85.assets/image-20220813184204764.png)

感觉这次可以了！

试试 `make`

![image-20220813184553852](mitsuba%20%E5%AE%89%E8%A3%85.assets/image-20220813184553852.png)

突破！	

![image-20220813184829647](mitsuba%20%E5%AE%89%E8%A3%85.assets/image-20220813184829647.png)

成了！！！

---

应该是哪里设置的问题， 就是导致 `cmake` 找 `openexr` 的时候， 找到的是 `mitsuba2` 里的， 而不是官方库里的。

![image-20220813200244635](mitsuba%20%E5%AE%89%E8%A3%85.assets/image-20220813200244635.png)

应该是 `PATH`设置， 太前面了， 要放后面去。

![image-20220813200427338](mitsuba%20%E5%AE%89%E8%A3%85.assets/image-20220813200427338.png)

`setpath.sh` 写得问题。

这也解释了为什么在 `ccmake` 的时候， 会卡在 `reading openexr` 的地方。

所以， 所以， 总结， `pthread` 是没有问题的， `not found in pthreads` 是`ok`的， 下面也有写， `THREAD` 是有的。

问题在于， 

**1. 不能使用 clang 编译！！！ 用 gcc g++ 都可以。**

**2. /usr/local/mitsuba-2/build/dist/libIlmImf.so， 优先找到了这个文件， 所以把它先重命名掉， 让 cmake 去找库里的， make 结束以后， 再重命名回来。**

**3. 其他的， 根据 cmake 日志， 缺啥补啥。**

---

##### render

![image-20220813191115018](mitsuba%20%E5%AE%89%E8%A3%85.assets/image-20220813191115018.png)

应该不是内存不够， 我把采样点从 `2084` 换成 `20`， 还是不行。

可能是 `optix` 没有导入？

---

##### 编译 mitsuba2 的时候， 把 optix 编译进去

我一直在想， `mitsuba 2` 到底怎么知道 `optix` 的路径的？ 到底怎么调用的？

我都没有设置 `optix` 路径这一过程。

而且， 我把 `optix` 的路径， `build/bin build/lib build/include include` 各种路径都加进 `PATH` 里了， 还是没有用。

![image-20220818000058935](mitsuba%20%E5%AE%89%E8%A3%85.assets/image-20220818000058935.png)

我就感觉很奇怪， 很可能就是在编译 `mitsuba2` 的时候， 直接编译进去的。

[How to Build Blender with Cuda and Optix on Ubuntu](https://skwrites.in/how-to-build-blender-with-cuda-and-optix-on-ubuntu/)

在这里， 我看到编译 `blender` 的时候， 是有一起编译 `optix` 的做法的。

![image-20220818000249566](mitsuba%20%E5%AE%89%E8%A3%85.assets/image-20220818000249566.png)

所以我就去看 `mitsuba2` 的文档， 但是没有找到这样类似的解释， 去`github`也没看到有人有类似的问题， 因为我发现网上大部分的教程和 `github issue` 都是基于 `windows` 系统的。

然后看了 `CMakeList.txt` 等相关文件， 也没有看出来什么。

终于！ https://bytemeta.vip/repo/mitsuba-renderer/mitsuba2/issues/569

在这个问答里， 看到了一个编译指令！

![image-20220818000507474](mitsuba%20%E5%AE%89%E8%A3%85.assets/image-20220818000507474.png)

```bash
cmake .. -DCMAKE_CUDA_ARCHITEXTURES=86 -DMTS_USE_OPTIX_HEADERS=1 -DMTS_OPTIX_PATH={some absolute path that contains the directory of /include/optix.h}
```

这就是我想要的！ 感觉可行啊！

改编一下：

```bash
cmake -GNinja .. -DMTS_USE_OPTIX_HEADERS=1 -DMTS_OPTIX_PATH=/usr/local/NVIDIA-OptiX-SDK-7.5.0-linux64-x86_64
```

![image-20220817235847453](mitsuba%20%E5%AE%89%E8%A3%85.assets/image-20220817235847453.png) 

`cmake` 的日志也不一样了！ 多了 `OptiX header files will be used.`

---

![image-20220818000727337](mitsuba%20%E5%AE%89%E8%A3%85.assets/image-20220818000727337.png)

报错。

感觉可能是版本问题， 我这里是最新的 `optix 7.5` 的。

文档也没写具体， 就写 `optix7`

那我就用 `optix7.0` 试一下。

![image-20220818001635876](mitsuba%20%E5%AE%89%E8%A3%85.assets/image-20220818001635876.png)

[NVIDIA OptiX™ Legacy Downloads](https://developer.nvidia.com/designworks/optix/downloads/legacy)

---

![image-20220818002537747](mitsuba%20%E5%AE%89%E8%A3%85.assets/image-20220818002537747.png)

`mitsuba2` 编译成功了！

![image-20220818002625449](mitsuba%20%E5%AE%89%E8%A3%85.assets/image-20220818002625449.png)

XXX， 我配置好了 gpu， 把 sample 降到 4， 可以渲染 一个球。

2048 个球， 降到4 也没用， 会说：

![image-20220818010752504](mitsuba%20%E5%AE%89%E8%A3%85.assets/image-20220818010752504.png)

采样点下降， 渲染出来的很粗糙!

![image-20220818010818713](mitsuba%20%E5%AE%89%E8%A3%85.assets/image-20220818010818713.png)

---

## mitsuba3

![image-20220830145320036](mitsuba%20%E5%AE%89%E8%A3%85.assets/image-20220830145320036.png)

3 的官方文档就有写的。

两种方式， 或者 cmake 的时候就编译进去。