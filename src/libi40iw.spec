Name: libi40iw
Version: 0.5.227 
Release: 1%{?dist}
Summary: Intel Ethernet Connection X722 RDMA Userspace Library

Group: System Environment/Libraries
License: BSD or GPLv2
Url: http://www.openfabrics.org/
Source: http://www.openfabrics.org/downloads/libi40iw/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: libibverbs-devel

%description
libi40iw provides a device-specific RDMA userspace library for Intel
Ethernet Connection X722 for use with the libibverbs library.

%package devel-static
Summary: Development files for the libi40iw library
Group: System Environment/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel-static
Static version of libi40iw that may be linked directly to an
application, which may be useful for debugging.

%prep
%setup -q -n %{name}-%{version}

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
# remove unpackaged files from the buildroot
rm -f %{buildroot}%{_libdir}/*.la %{buildroot}%{_libdir}/libi40iw.so

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_libdir}/libi40iw*.so
%config %{_sysconfdir}/libibverbs.d/i40iw.driver
%license COPYING
%doc AUTHORS

%files devel-static
%defattr(-,root,root,-)
%{_libdir}/libi40iw*.a

%changelog
* Mon Aug 1 2016 Chien Tin Tung <chien.tin.tung@intel.com> - 0.5.227-1
- Fix and refactor error patch in i40iw_ucreate_qp

* Fri Jul 22 2016 Tatyana Nikolova <tatyana.e.nikolova@intel.com> - 0.5.226-1
- Remove code for inline data size greater than 64B
- Replace sysconf call with the supported page size
- Add return code check for pthread_spin calls

* Wed Jul 6 2016 Tatyana Nikolova <tatyana.e.nikolova@intel.com> - 0.5.225-1
- Add isa dependency to subpackage
- Remove "rm -rf buildroot" from the install section

* Thu Jun 30 2016 Tatyana Nikolova <tatyana.e.nikolova@intel.com> - 0.5.224-1
- Add BSD license text to COPYING
- Clean up the AM_CFLAGS settings
- Minor fixes to the spec.in, including license, config and url entries

* Mon May 23 2016 Tatyana Nikolova <tatyana.e.nikolova@intel.com> - 0.5.223-1
- Initial public release of libi40iw
