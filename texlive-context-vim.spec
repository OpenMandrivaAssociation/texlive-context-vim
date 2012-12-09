# revision 27231
# category ConTeXt
# catalog-ctan /macros/context/contrib/context-vim
# catalog-date 2012-05-29 08:52:39 +0200
# catalog-license bsd
# catalog-version undef
Name:		texlive-context-vim
Version:	20120529
Release:	1
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


%changelog
* Tue Aug 07 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120529-1
+ Revision: 812178
- Update to latest release.

* Mon Jun 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120502-1
+ Revision: 804541
- Update to latest release.

* Thu Feb 23 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120212-1
+ Revision: 779436
- Update to latest release.

* Tue Jan 31 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120115-2
+ Revision: 770138
- Update to latest upstream package

* Thu Jan 19 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120115-1
+ Revision: 762597
- Update to latest upstream package

* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111205-3
+ Revision: 750533
- Rebuild to reduce used resources

* Mon Dec 26 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111205-2
+ Revision: 745204
- texlive-context-vim

* Fri Dec 09 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111205-1
+ Revision: 739739
- texlive-context-vim

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111021-1
+ Revision: 718146
- texlive-context-vim
- texlive-context-vim
- texlive-context-vim
- texlive-context-vim

