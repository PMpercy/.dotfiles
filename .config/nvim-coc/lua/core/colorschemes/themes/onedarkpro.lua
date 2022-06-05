local status_ok, onedarkpro = pcall(require, 'onedarkpro')
if not status_ok then
    return
end

onedarkpro.setup({
  	-- Theme can be overwritten with 'onedark' or 'onelight' as a string
  	theme = function()
    	if vim.o.background == "dark" then
      		return "onedark"
    	else
      		return "onelight"
    	end
  	end,
  	colors = {}, -- Override default colors by specifying colors for 'onelight' or 'onedark' themes
  	hlgroups = {}, -- Override default highlight groups
  	filetype_hlgroups = {}, -- Override default highlight groups for specific filetypes
  	plugins = { -- Override which plugins highlight groups are loaded
      	native_lsp = true,
      	polygot = true,
      	treesitter = true,
      	-- NOTE: Other plugins have been omitted for brevity
  	},
  	styles = {
      	strings = "italic", -- Style that is applied to strings
      	comments = "NONE", -- Style that is applied to comments
      	keywords = "italic", -- Style that is applied to keywords
      	functions = "italic", -- Style that is applied to functions
      	variables = "italic", -- Style that is applied to variables
  	},
  	options = {
      	bold = true, -- Use the themes opinionated bold styles?
      	italic = true, -- Use the themes opinionated italic styles?
      	underline = false, -- Use the themes opinionated underline styles?
      	undercurl = false, -- Use the themes opinionated undercurl styles?
      	cursorline = true, -- Use cursorline highlighting?
      	transparency = true, -- Use a transparent background?
      	terminal_colors = false, -- Use the theme's colors for Neovim's :terminal?
      	window_unfocussed_color = true, -- When the window is out of focus, change the normal background?
  	},
	plugins = {
		all = true
	}
})
onedarkpro.load()
