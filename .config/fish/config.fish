if status is-interactive
    # Commands to run in interactive sessions can go here
end
#starship init fish | source

# --- Alias

alias grep='grep --color=auto'
alias cat='bat --style=plain --paging=never'
alias ls='exa --group-directories-first'
alias tree='exa -T'
alias l='exa --group-directories-first -la'
# - git
alias clone='git clone'
alias commit='git commit -m'
alias add='git add'
alias g-status='git status'

alias upgrade='yay -Syyyu'
alias app='yay -Sy'
alias rg='ranger'
 
alias vi='nvim'
alias rg='ranger'
alias py='python'
alias pi='pip'

# - exports
export EDITOR=nvim


# new line and prompt
set -g theme_newline_cursor yes
set -g theme_newline_prompt '$ '

#
set -g theme_color_scheme dark
set -g theme_display_date no

function fish_greeting
    set_color $fish_color_autosuggestion
    #echo "Bienvenido :)"
    set_color normal
end
