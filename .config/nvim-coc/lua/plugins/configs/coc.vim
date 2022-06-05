
autocmd CursorHold * silent call CocActionAsync('highlight')

inoremap <silent><expr> <TAB>
    \ pumvisible() ? "\<C-n>" :
    \ CheckBackspace() ? "\<TAB>" :
    \ coc#refresh()
inoremap <expr><S-TAB> pumvisible() ? "\<C-p>": "\<C-h>"

function! CheckBackspace() abort
    let col = col('.') -1
    return !col || getline('.')[col -1] =~# '\s'
endfunction

" Use <ctrl+space> to tigger competion
if has('nvim')
    inoremap <silent><expr> <c-space> coc#refresh()
else
    inoremap <silent><expr> <c-@> coc#refresh()
endif


