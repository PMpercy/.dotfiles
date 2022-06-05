local status_ok, catppuccin = pcall(require, 'catppuccin')
if not status_ok then
    return
end

catppuccin.setup({
    term_colors = true,
    transparent_background = true,
    styles = {
        comment = "NONE",
        functions = "NONE",
        keywords = "NONE",
        strings = "NONE",
        variables = "NONE"
    },
    integrations = {
        treesitter = false,
        nvimtree = {
            enabled = true,
            transparent_panel = true
        }
    }
})

vim.cmd[[colorscheme catppuccin]]
