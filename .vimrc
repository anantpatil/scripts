" set soft wrap, automatic line break
" show breaks in like with ...
" set nolist as it messes up with linebreak
syntax on
set wrap lbr nolist showbreak=…
set ai sw=4 wm=5 sm
set smarttab
set textwidth=72
"colorscheme slate
if has('gui_running')
    "For GUI, colorscheme is solarized dark
    colorscheme solarized
    set background=dark
else
    colorscheme default
endif
"set guifont=Inconsolata-dz\ Medium\ 9
"set guifont=monospace\ Medium\ 9
set guifont=Source\ Code\ Pro\ Semi-Bold\ 9

"to automatically format text as and when edited.
" set formatoptions+=a 

" highlight search matches
set hlsearch

" Press Space to turn off highlighting and clear any
" message already displayed.  
:nnoremap <silent> <Space> :nohlsearch<Bar>:echo<CR>

" Press F4 to toggle highlighting on/off, and show current value.
:noremap <F4> :set hlsearch! hlsearch?<CR>

" Following will map F8 to hghlight the occurences of current word
" * and # are used to search the current word forward and backword
:nnoremap <F8> :let @/='\<<C-R>=expand("<cword>")<CR>\>'<CR>:set hls<CR>

" set lang to en_gb
setlocal spelllang=en_gb

" Press F2 to toggle spell check on/off, and show current value.
:noremap <F2> :setlocal spell! spell?<CR>


" Press F7 to toggle syntax highlighting on/off
:map <F7> :if exists("g:syntax_on") <Bar>
    \   syntax off <Bar>
    \ else <Bar>
    \   syntax enable <Bar>
    \ endif <CR>

" Use external paragraph formatter par
" par is powerful paragraph formatter
" set formatprg=par\ -w40 for width 40
" use gq to format using par and gw to use vim's formatter
" q option to handle nested quotations in plain text e-mail.
" Use j option to justify text
" repeat characters in bodiless lines
" set formatprg=par\ -w72qrj
" i have kep for q option for mail editing
set formatprg=par\ -w72q

" load vimrc for editing on one command ,v
" to source vimrc file, issue :source $MYVIMRC
let mapleader = ","
nmap <leader>v :tabedit $MYVIMRC<CR>

" set incremental search
set incsearch

" Pathogen
execute pathogen#infect()

" Open NERD_Tree when no files are specified
autocmd vimenter * if !argc() | NERDTree | endif

" Open nerd tree with Ctrl-N
map <C-n> :NERDTreeToggle<CR>

" For ctrl-P
set runtimepath^=~/.vim/bundle/ctrlp.vim

" To have relative line numbers in normal mode for fast movement
" set relativenumber
autocmd insertEnter * :set number
autocmd insertLeave * :set relativenumber

"When not in focus just show line number,
:au FocusLost * :set number
:au FocusGained * :set relativenumber
