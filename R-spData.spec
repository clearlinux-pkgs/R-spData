#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-spData
Version  : 0.3.0
Release  : 24
URL      : https://cran.r-project.org/src/contrib/spData_0.3.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/spData_0.3.0.tar.gz
Summary  : Datasets for Spatial Analysis
Group    : Development/Tools
License  : CC0-1.0
BuildRequires : buildreq-R

%description
spData
======
[![Build Status](https://travis-ci.org/Nowosad/spData.png?branch=master)](https://travis-ci.org/Nowosad/spData) [![CRAN version](http://www.r-pkg.org/badges/version/spData)](https://cran.r-project.org/package=spData) [![CRAN RStudio mirror downloads](http://cranlogs.r-pkg.org/badges/spData)](https://cran.r-project.org/package=spData)

%prep
%setup -q -c -n spData

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552940431

%install
export SOURCE_DATE_EPOCH=1552940431
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library spData
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library spData
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library spData
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  spData || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/spData/DESCRIPTION
/usr/lib64/R/library/spData/INDEX
/usr/lib64/R/library/spData/Meta/Rd.rds
/usr/lib64/R/library/spData/Meta/data.rds
/usr/lib64/R/library/spData/Meta/features.rds
/usr/lib64/R/library/spData/Meta/hsearch.rds
/usr/lib64/R/library/spData/Meta/links.rds
/usr/lib64/R/library/spData/Meta/nsInfo.rds
/usr/lib64/R/library/spData/Meta/package.rds
/usr/lib64/R/library/spData/NAMESPACE
/usr/lib64/R/library/spData/R/spData
/usr/lib64/R/library/spData/R/spData.rdb
/usr/lib64/R/library/spData/R/spData.rdx
/usr/lib64/R/library/spData/README
/usr/lib64/R/library/spData/data/Rdata.rdb
/usr/lib64/R/library/spData/data/Rdata.rds
/usr/lib64/R/library/spData/data/Rdata.rdx
/usr/lib64/R/library/spData/data/datalist
/usr/lib64/R/library/spData/help/AnIndex
/usr/lib64/R/library/spData/help/aliases.rds
/usr/lib64/R/library/spData/help/paths.rds
/usr/lib64/R/library/spData/help/spData.rdb
/usr/lib64/R/library/spData/help/spData.rdx
/usr/lib64/R/library/spData/html/00Index.html
/usr/lib64/R/library/spData/html/R.css
/usr/lib64/R/library/spData/misc/cycle_hire_xy.csv
/usr/lib64/R/library/spData/misc/nyadjwts.dbf
/usr/lib64/R/library/spData/misc/nydata.dbf
/usr/lib64/R/library/spData/misc/world_wkt.csv
/usr/lib64/R/library/spData/misc/worldbank_df.csv
/usr/lib64/R/library/spData/shapes/NY8_bna_utm18.gpkg
/usr/lib64/R/library/spData/shapes/NY8_utm18.dbf
/usr/lib64/R/library/spData/shapes/NY8_utm18.prj
/usr/lib64/R/library/spData/shapes/NY8_utm18.shp
/usr/lib64/R/library/spData/shapes/NY8_utm18.shx
/usr/lib64/R/library/spData/shapes/auckland.dbf
/usr/lib64/R/library/spData/shapes/auckland.shp
/usr/lib64/R/library/spData/shapes/auckland.shx
/usr/lib64/R/library/spData/shapes/baltim.dbf
/usr/lib64/R/library/spData/shapes/baltim.shp
/usr/lib64/R/library/spData/shapes/baltim.shx
/usr/lib64/R/library/spData/shapes/boston_tracts.dbf
/usr/lib64/R/library/spData/shapes/boston_tracts.prj
/usr/lib64/R/library/spData/shapes/boston_tracts.shp
/usr/lib64/R/library/spData/shapes/boston_tracts.shx
/usr/lib64/R/library/spData/shapes/columbus.dbf
/usr/lib64/R/library/spData/shapes/columbus.shp
/usr/lib64/R/library/spData/shapes/columbus.shx
/usr/lib64/R/library/spData/shapes/cycle_hire.geojson
/usr/lib64/R/library/spData/shapes/cycle_hire_osm.geojson
/usr/lib64/R/library/spData/shapes/eire.dbf
/usr/lib64/R/library/spData/shapes/eire.shp
/usr/lib64/R/library/spData/shapes/eire.shx
/usr/lib64/R/library/spData/shapes/sids.dbf
/usr/lib64/R/library/spData/shapes/sids.shp
/usr/lib64/R/library/spData/shapes/sids.shx
/usr/lib64/R/library/spData/shapes/wheat.dbf
/usr/lib64/R/library/spData/shapes/wheat.shp
/usr/lib64/R/library/spData/shapes/wheat.shx
/usr/lib64/R/library/spData/shapes/world.dbf
/usr/lib64/R/library/spData/shapes/world.gpkg
/usr/lib64/R/library/spData/shapes/world.prj
/usr/lib64/R/library/spData/shapes/world.shp
/usr/lib64/R/library/spData/shapes/world.shx
/usr/lib64/R/library/spData/weights/NY_nb.gal
/usr/lib64/R/library/spData/weights/baltk4.GWT
/usr/lib64/R/library/spData/weights/columbus.gal
/usr/lib64/R/library/spData/weights/ncCC89.gal
/usr/lib64/R/library/spData/weights/ncCR85.gal
