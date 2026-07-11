%global tl_name lshort-czech
%global tl_revision 55643

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.27
Release:	%{tl_revision}.1
Summary:	Czech translation of the Short Introduction to LaTeX2e
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/lshort/czech
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-czech.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-czech.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is the Czech translation of "A Short Introduction to LaTeX2e".

