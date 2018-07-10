# revision 29984
# category ConTeXt
# catalog-ctan /macros/context/contrib/context-vim
# catalog-date 2012-08-13 18:31:33 +0200
# catalog-license bsd
# catalog-version undef
Name:		texlive-context-vim
Version:	20171129
Release:	2
Summary:	Generate Context syntax highlighting code from vim
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/context/contrib/context-vim
License:	BSD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-vim.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-vim.doc.tar.xz
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
%{_texmfdistdir}/tex/context/third/vim/2context.vim
%{_texmfdistdir}/tex/context/third/vim/t-syntax-groups.tex
%{_texmfdistdir}/tex/context/third/vim/t-syntax-highlight.mkii
%{_texmfdistdir}/tex/context/third/vim/t-syntax-highlight.mkiv
%{_texmfdistdir}/tex/context/third/vim/t-vim.tex
%doc %{_texmfdistdir}/doc/context/third/vim/vim.txt

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
