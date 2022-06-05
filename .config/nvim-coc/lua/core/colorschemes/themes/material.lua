local status_ok, material = pcall(require, 'material')
if not status_ok then
    return
end

material.setup({
	contrast = {
		sidebars = true,
		cursor_line = true,
		popup_menu = true,
	},
	italics = {
		comments = false,
		keywords = false,
		functions = false,
		strings = false,
		variables = false,
	},
    disable = {
		colored_cursor = false, -- Disable the colored cursor
		borders = false, -- Disable borders between verticaly split windows
		background = false, -- Prevent the theme from setting the background (NeoVim then uses your teminal background)
		term_colors = true, -- Prevent the theme from setting terminal colors
		eob_lines = false -- Hide the end-of-buffer lines
	},
	async_loading = true,

    custom_highlights = {
        --NvimTreeNormal = { bg = '#fff'},
        CursorLine = { fg = '#fff', gui = 'underline'},
        --LineNr = { bg = "#FF0000"}
    },

})

-- darker, lighter, oceanic, palenight, deep ocean,
vim.g.material_style = "darker"
vim.cmd 'colorscheme material'


