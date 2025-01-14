Name:		texlive-context-vim
Version:	62071
Release:	2
Summary:	Generate Context syntax highlighting code from vim
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/context/contrib/context-vim
License:	BSD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-vim.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-vim.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-context
Requires:	texlive-context-filter

%description
ConTeXt has excellent pretty printing capabilities for many
languages. The code for pretty printing is written in TeX, and
due to catcode juggling, such verbatim typesetting is perhaps
the trickiest part of TeX. This makes it difficult for a
"normal" user to define syntax highlighting rules for a new
language. This module takes the onus of defining syntax
highlighting rules away from the user and uses ViM editor to
generate the syntax highlighting. There is a helper
2context.vim script to do the syntax parsing in ViM.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/context/third/vim
%doc %{_texmfdistdir}/doc/context/third/vim

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
