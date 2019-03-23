set nocompatible
filetype off

set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

Plugin 'VundleVim/Vundle.vim'
Plugin 'powerline/powerline', {'rtp': 'powerline/bindings/vim/'}
let g:Powerline_symbols = "fancy"
Plugin 'klen/python-mode'
let g:pymode_folding = 0
let g:pymode_rope = 0
let g:pymode_options_max_line_length = 999
Plugin 'tell-k/vim-autopep8'
Plugin 'scrooloose/syntastic'
Plugin 'Valloric/YouCompleteMe'
Plugin 'vim-scripts/indentpython.vim'

call vundle#end()
filetype plugin indent on

set expandtab
set tabstop=4
set softtabstop=4
set shiftwidth=4

set ls=2
set incsearch

syntax on

set nu
set ai
set ruler
set nowrap
set autoread
set cursorline
set clipboard=unnamed
set backspace=2
set laststatus=2
set scrolloff=3
set t_Co=256
set ttymouse=xterm2
set mouse=a

hi LineNr ctermfg=Blue
hi CursorLineNr cterm=bold ctermfg=Green ctermbg=DarkGray

nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>
