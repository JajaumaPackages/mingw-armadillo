%?mingw_package_header

Name:           mingw-armadillo
Version:        7.700.0
Release:        1%{?dist}
Summary:        MinGW port of Armadillo C++ linear algebra library

License:        MPLv2.0
URL:            http://arma.sourceforge.net/
Source0:        http://sourceforge.net/projects/arma/files/armadillo-%{version}.tar.xz

BuildRequires:  mingw32-filesystem
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-gcc-c++
BuildRequires:  cmake

BuildArch:      noarch

%description
MinGW Windows port of Armadillo C++ linear algebra library.

# Win32
%package -n mingw32-armadillo
Summary:        32-bit version of Armadillo C++ linear algebra library for Windows

%description -n mingw32-armadillo
%mingw32_description

# Win64
%package -n mingw64-armadillo
Summary:        64-bit version of Armadillo C++ linear algebra library for Windows

%description -n mingw64-armadillo
%mingw64_description

%?mingw_debug_package

%prep
%setup -qn armadillo-%{version}

%build
%mingw_cmake
%mingw_make %{?_smp_mflags}

%install
%mingw_make install DESTDIR=%{buildroot}

# Win32
%files -n mingw32-armadillo
%{mingw32_bindir}/libarmadillo.dll
%{mingw32_includedir}/armadillo
%{mingw32_includedir}/armadillo_bits/
%{mingw32_libdir}/libarmadillo.dll.a
%{mingw32_libdir}/pkgconfig/armadillo.pc
%{mingw32_datadir}/Armadillo/

# Win64
%files -n mingw64-armadillo
%{mingw64_bindir}/libarmadillo.dll
%{mingw64_includedir}/armadillo
%{mingw64_includedir}/armadillo_bits/
%{mingw64_libdir}/libarmadillo.dll.a
%{mingw64_libdir}/pkgconfig/armadillo.pc
%{mingw64_datadir}/Armadillo/

%changelog
* Tue Feb 07 2017 Jajauma's Packages <jajauma@yandex.ru> - 7.700.0-1
- Initial release
