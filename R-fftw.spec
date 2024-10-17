%global packname  fftw
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.0.3
Release:          1
Summary:          Fast FFT and DCT based on FFTW
Group:            Sciences/Mathematics
License:          GPLv2
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-3.tar.gz

BuildRequires:    R-devel Rmath-devel texlive-collection-latex 
BuildRequires:    pkgconfig(fftw3)


%description
Provides a simple and efficient wrapper around the fastest Fourier
transform in the west (FFTW) library.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/unittests
%{rlibdir}/%{packname}/libs
