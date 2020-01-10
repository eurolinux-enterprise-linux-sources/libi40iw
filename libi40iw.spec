Name: libi40iw
Version: 0.5.227
Release: 2%{?dist}
Summary: Intel Ethernet Connection X722 RDMA Userspace Library

Group: System Environment/Libraries
License: BSD or GPLv2
Url: http://www.openfabrics.org/
Source: http://www.openfabrics.org/downloads/libi40iw/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: libibverbs-devel
Provides: libibverbs-driver.%{_arch}

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
%setup -q

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
* Fri Aug 09 2016 Jarod Wilson <jarod@redhat.com> - 0.5.227-2
- Add virtual Provides: libibverbs-driver.arch
- Resolves: rhbz#1374472

* Mon Aug 01 2016 Jarod Wilson <jarod@redhat.com> - 0.5.227-1
- Update to upstream version 0.5.227 for final version of memleak fixes

* Thu Jul 28 2016 Jarod Wilson <jarod@redhat.com> - 0.5.226-4
- Now do it so we don't leak iwuqp in another error path

* Thu Jul 28 2016 Jarod Wilson <jarod@redhat.com> - 0.5.226-3
- Fix it even better, so we don't try to free iwuqp twice

* Thu Jul 28 2016 Jarod Wilson <jarod@redhat.com> - 0.5.226-2
- Fix up memleak fix

* Wed Jul 27 2016 Jarod Wilson <jarod@redhat.com> - 0.5.226-1
- Update to upstream version 0.5.226 for coverity-inspired fixes

* Wed Jul 20 2016 Jarod Wilson <jarod@redhat.com> - 0.5.225-2
- Initial Red Hat build for EL7

* Wed Jul 06 2016 Tatyana Nikolova <tatyana.e.nikolova@intel.com> - 0.5.225-1
- Add isa dependency to subpackage
- Remove "rm -rf buildroot" from the install section

* Thu Jun 30 2016 Tatyana Nikolova <tatyana.e.nikolova@intel.com> - 0.5.224-1
- Add BSD license text to COPYING
- Clean up the AM_CFLAGS settings
- Minor fixes to the spec.in, including license, config and url entries

* Mon May 23 2016 Tatyana Nikolova <tatyana.e.nikolova@intel.com> - 0.5.223-1
- Initial public release of libi40iw
