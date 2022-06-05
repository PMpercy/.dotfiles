
local status_ok, colors = pcall(require, 'material.colors')
if not status_ok then
    return
end

local Ocean = {
	normal = {
		a = { fg = colors.accent, bg = colors.bg, gui = 'bold' },
		b = { fg = colors.title, bg = colors.bg, gui = 'bold' },
		c = { fg = colors.commnets, bg = colors.bg, gui = 'bold' }
	},
	insert = {
		a = { fg = colors.green, bg = colors.bg, gui = 'bold'},
		b = { fg = colors.title, bg = colors.bg, gui = 'bold'}
	},
	replace = {
		a = { fg = colors.red, bg = colors.bg, gui = 'bold'},
		b = { fg = colors.title, bg = colors.bg }
	},
	visual = {
		a = { fg = colors.purple, bg = colors.bg, gui = 'bold' },
		b = { fg = colors.title, bg = colors.bg }
	},
	command = {
		a = { fg = colors.yellow, bg = colors.bg, gui = 'bold' },
		b = { fg = colors.title, bg = colors.bg, gui = 'bold'}
	},
	inactive = {
		a = { fg = colors.disabled, bg = colors.bg },
		b = { fg = colors.disabled, bg = colors.bg },
		c = { fg = colors.disabled, bg = colors.bg }
	}

}

return Ocean
