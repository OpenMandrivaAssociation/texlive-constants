# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/constants
# catalog-date 2008-08-18 10:38:42 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-constants
Version:	1.0
Release:	11
Summary:	Automatic numbering of constants
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/constants
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/constants.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/constants.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/constants.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a way to number constants in a
mathematical proof automatically, with a system for
labelling/referencing. In addition, several families of
constants (with different symbols) may be defined.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/constants/constants.sty
%doc %{_texmfdistdir}/doc/latex/constants/README
%doc %{_texmfdistdir}/doc/latex/constants/constants.pdf
#- source
%doc %{_texmfdistdir}/source/latex/constants/constants.dtx
%doc %{_texmfdistdir}/source/latex/constants/constants.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 750450
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 718120
- texlive-constants
- texlive-constants
- texlive-constants
- texlive-constants

