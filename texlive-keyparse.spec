Name:		texlive-keyparse
Version:	60277
Release:	1
Summary:	Key based parser
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/keyparse
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/keyparse.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/keyparse.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/keyparse.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX package provides an interface to define and evaluate
key-based replacement rules. It can be used to parse the
argument specification of a document command.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/keyparse
%{_texmfdistdir}/tex/latex/keyparse
%doc %{_texmfdistdir}/doc/latex/keyparse

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
