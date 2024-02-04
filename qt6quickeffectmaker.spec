#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v3
# autospec commit: 750e50d
#
Name     : qt6quickeffectmaker
Version  : 6.6.1
Release  : 7
URL      : https://download.qt.io/official_releases/qt/6.6/6.6.1/submodules/qtquickeffectmaker-everywhere-src-6.6.1.tar.xz
Source0  : https://download.qt.io/official_releases/qt/6.6/6.6.1/submodules/qtquickeffectmaker-everywhere-src-6.6.1.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GFDL-1.3 GPL-3.0
Requires: qt6quickeffectmaker-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : mesa-dev
BuildRequires : qt6base-dev
BuildRequires : qt6declarative-dev
BuildRequires : qt6quick3d-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package license
Summary: license components for the qt6quickeffectmaker package.
Group: Default

%description license
license components for the qt6quickeffectmaker package.


%prep
%setup -q -n qtquickeffectmaker-everywhere-src-6.6.1
cd %{_builddir}/qtquickeffectmaker-everywhere-src-6.6.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1707067119
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1707067119
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qt6quickeffectmaker
cp %{_builddir}/qtquickeffectmaker-everywhere-src-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/qt6quickeffectmaker/b073f11f0c81a95ab5e32aa6b5d23a5955a95274 || :
cp %{_builddir}/qtquickeffectmaker-everywhere-src-%{version}/LICENSES/GFDL-1.3-no-invariants-only.txt %{buildroot}/usr/share/package-licenses/qt6quickeffectmaker/715f995f11805ee85601834220c43b082f457ea3 || :
cp %{_builddir}/qtquickeffectmaker-everywhere-src-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/qt6quickeffectmaker/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/V3/usr/lib64/qt6/bin/qqem
/usr/lib64/qt6/bin/qqem
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/basic/brightness_contrast.qen
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/basic/colorize.qen
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/basic/coloroverlay.qen
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/basic/desaturate.qen
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/basic/displace.qen
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/basic/dropshadow.qen
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/basic/fastblur.qen
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/basic/gamma_adjust.qen
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/basic/innershadow.qen
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/basic/leveladjust.qen
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/basic/mipmapblur.qen
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/basic/mipmapdropshadow.qen
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/basic/multieffect.qen
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/basic/noise.qen
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/basic/opacitymask.qen
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/basic/thresholdmask.qen
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/basic/vignette.qen
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/common/0_custom.qen
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/common/BlurHelper.qml
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/common/blurhelper.qen
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/common/bluritems.frag
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/common/bluritems.frag.qsb
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/common/bluritems.vert
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/common/bluritems.vert.qsb
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/common/mathhelper.qen
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/common/noisehelper.qen
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/extra/bend.qen
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/extra/colorlut.qen
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/extra/ledscreen.qen
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/extra/normalmapping.qen
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/extra/sunburst.qen
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/extra/swirl.qen
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/images/blackcircle.png
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/images/clouds.png
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/images/fog.png
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/images/fog2.png
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/images/lava.png
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/images/lut_256_apocalypse.png
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/images/lut_256_bleach.png
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/images/lut_256_bright.png
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/images/lut_256_cinematic1.png
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/images/lut_256_cinematic2.png
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/images/lut_256_cinematic3.png
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/images/lut_256_cold.png
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/images/lut_256_drama.png
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/images/lut_256_fall.png
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/images/lut_256_horror.png
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/images/lut_256_neutral.png
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/images/lut_256_old.png
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/images/lut_256_sepia.png
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/images/lut_256_summer.png
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/images/lut_256_sunset.png
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/images/lut_256_tealorange.png
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/images/lut_256_vibrant.png
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/images/lut_256_vintage1.png
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/images/lut_256_vintage2.png
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/images/lut_256_vintage3.png
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/images/lut_256_vintagebw.png
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/images/lut_256_warm.png
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/images/lut_512_apocalypse.png
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/images/lut_512_bleach.png
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/images/lut_512_bright.png
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/images/lut_512_cinematic1.png
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/images/lut_512_cinematic2.png
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/images/lut_512_cinematic3.png
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/images/lut_512_cold.png
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/images/lut_512_drama.png
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/images/lut_512_fall.png
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/images/lut_512_horror.png
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/images/lut_512_neutral.png
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/images/lut_512_old.png
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/images/lut_512_sepia.png
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/images/lut_512_summer.png
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/images/lut_512_sunset.png
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/images/lut_512_tealorange.png
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/images/lut_512_vibrant.png
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/images/lut_512_vintage1.png
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/images/lut_512_vintage2.png
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/images/lut_512_vintage3.png
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/images/lut_512_vintagebw.png
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/images/lut_512_warm.png
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/images/mask.png
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/images/mask2.png
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/images/qt_logo_green_rgb.png
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/images/qt_logo_green_rgb_n.png
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/images/quit_logo.png
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/images/quit_logo_n.png
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/images/rain.png
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/images/scratches_n.png
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/images/whitecircle.png
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/nature/clouds.qen
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/nature/electricclouds.qen
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/nature/fog.qen
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/nature/lava.qen
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/nature/plasma.qen
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/nature/rain.qen
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/nature/seareflection.qen
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/nature/snowing.qen
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/nature/thunder.qen
/usr/lib64/qt6/qml/QtQuickEffectMaker/defaultnodes/nature/water.qen

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qt6quickeffectmaker/715f995f11805ee85601834220c43b082f457ea3
/usr/share/package-licenses/qt6quickeffectmaker/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/qt6quickeffectmaker/b073f11f0c81a95ab5e32aa6b5d23a5955a95274
