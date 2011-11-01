Name:		texlive-context-vim
Version:	20111021
Release:	1
Summary:	Generate Context syntax highlighting code from vim
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/context/contrib/context-vim
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-vim.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-vim.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Requires:	texlive-context-filter
Requires:	texlive-context
Conflicts:	texlive-texmf <= 20110705-3
Requires(post):	texlive-context.bin

%description
ConTeXt has excellent pretty printing capabilities for many
languages. The code for pretty printing is written in TeX, and
due to catcode juggling, such verbatim typesetting is perhaps
the trickiest part of TeX. This makes it difficult for a
"normal" user to define syntax highlighting rules for a new
language. This module takes the onus of defining syntax
highlighting rules away from the user and uses ViM editor to
generate the syntax highlighting. There is a helper
2context.vim script to do the syntax parsing in ViM. This is a
stop-gap method, and hopefully with LuaTeX, things will be much
easier.

%pre
    %_texmf_mtxrun_pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mtxrun_post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mtxrun_pre
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mtxrun_post
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/context/third/vim/2context.vim
%{_texmfdistdir}/tex/context/third/vim/t-syntax-groups.tex
%{_texmfdistdir}/tex/context/third/vim/t-syntax-highlight.tex
%{_texmfdistdir}/tex/context/third/vim/t-vim.tex
%doc %{_texmfdistdir}/doc/context/third/vim/vim.txt

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
