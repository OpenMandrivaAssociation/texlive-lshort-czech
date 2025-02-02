Name:		texlive-lshort-czech
Version:	55643
Release:	2
Summary:	Czech translation of the "Short Introduction to LaTeX2e"
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/lshort/czech
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-czech.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-czech.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
This is the Czech translation of "A Short Introduction to
LaTeX2e".

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/lshort-czech/CHANGES
%doc %{_texmfdistdir}/doc/latex/lshort-czech/MANIFEST
%doc %{_texmfdistdir}/doc/latex/lshort-czech/Makefile
%doc %{_texmfdistdir}/doc/latex/lshort-czech/README
%doc %{_texmfdistdir}/doc/latex/lshort-czech/lshort-cs.pdf
%doc %{_texmfdistdir}/doc/latex/lshort-czech/src/appendix.tex
%doc %{_texmfdistdir}/doc/latex/lshort-czech/src/biblio.tex
%doc %{_texmfdistdir}/doc/latex/lshort-czech/src/contrib.tex
%doc %{_texmfdistdir}/doc/latex/lshort-czech/src/custom.tex
%doc %{_texmfdistdir}/doc/latex/lshort-czech/src/fancyhea.sty
%doc %{_texmfdistdir}/doc/latex/lshort-czech/src/graphic.tex
%doc %{_texmfdistdir}/doc/latex/lshort-czech/src/lshort-base.tex
%doc %{_texmfdistdir}/doc/latex/lshort-czech/src/lshort-cs-a5.tex
%doc %{_texmfdistdir}/doc/latex/lshort-czech/src/lshort-cs.ind
%doc %{_texmfdistdir}/doc/latex/lshort-czech/src/lshort-cs.tex
%doc %{_texmfdistdir}/doc/latex/lshort-czech/src/lshort.ist
%doc %{_texmfdistdir}/doc/latex/lshort-czech/src/lshort.sty
%doc %{_texmfdistdir}/doc/latex/lshort-czech/src/lssym.tex
%doc %{_texmfdistdir}/doc/latex/lshort-czech/src/math.tex
%doc %{_texmfdistdir}/doc/latex/lshort-czech/src/mylayout.sty
%doc %{_texmfdistdir}/doc/latex/lshort-czech/src/overview.tex
%doc %{_texmfdistdir}/doc/latex/lshort-czech/src/spec.tex
%doc %{_texmfdistdir}/doc/latex/lshort-czech/src/things.tex
%doc %{_texmfdistdir}/doc/latex/lshort-czech/src/title.tex
%doc %{_texmfdistdir}/doc/latex/lshort-czech/src/typeset.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
