Name:		texlive-constants
Version:	15878
Release:	2
Summary:	Automatic numbering of constants
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/constants
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/constants.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/constants.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/constants.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
