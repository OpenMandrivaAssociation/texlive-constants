# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/constants
# catalog-date 2008-08-18 10:38:42 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-constants
Version:	1.0
Release:	1
Summary:	Automatic numbering of constants
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/constants
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/constants.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/constants.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/constants.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package provides a way to number constants in a
mathematical proof automatically, with a system for
labelling/referencing. In addition, several families of
constants (with different symbols) may be defined.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/constants/constants.sty
%doc %{_texmfdistdir}/doc/latex/constants/README
%doc %{_texmfdistdir}/doc/latex/constants/constants.pdf
#- source
%doc %{_texmfdistdir}/source/latex/constants/constants.dtx
%doc %{_texmfdistdir}/source/latex/constants/constants.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
