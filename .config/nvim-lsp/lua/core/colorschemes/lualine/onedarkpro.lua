local status_ok, colors = pcall(require, 'onedarkpro')
if not status_ok then
    return
end

colors.get_colors()
local onedarkpro = {

	normal = {
		a = { bg = colors.bg, fg = colors.green },
		b = { bg = colors.bg, fg = colors.green },
		c = { bg = colors.bg, fg = colors.fg_sidebar },
	},

	insert = {
		a = { bg = colors.bg, fg = colors.blue },
		b = { bg = colors.bg, fg = colors.blue },
	},

	command = {
		a = { bg = colors.bg, fg = colors.purple },
		b = { bg = colors.bg, fg = colors.fg_gutter },
	},

	visual = {
		a = { bg = colors.bg, fg = colors.yellow },
		b = { bg = colors.bg, fg = colors.yellow },
	},

	replace = {
		a = { bg = colors.bg, fg = colors.red },
		b = { bg = colors.bg, fg = colors.fg_gutter },
	},

	inactive = {
		a = { bg = colors.bg, fg = colors.blue },
		b = { bg = colors.bg, fg = colors.fg_gutter, gui = "bold" },
		c = { bg = colors.bg, fg = colors.fg_gutter },
	}
}
return onedarkpro


