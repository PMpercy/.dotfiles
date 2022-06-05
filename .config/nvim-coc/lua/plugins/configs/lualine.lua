local status_ok, lualine = pcall(require, "lualine")
if not status_ok then
	return
end


local hide_in_width = function()
	return vim.fn.winwidth(0) > 80
end

local diagnostics = {
	"diagnostics",
   	sources = { "nvim_diagnostic", "coc" },
	symbols = { error = " ", warn = " ", info = " ", hint = " " },
	colored = true,
	update_in_insert = true,
	--always_visible = true,
}

local diff = {
	"diff",
	--colored = false,
	symbols = { added = " ", modified = " ", removed = " " }, -- changes diff symbols
    --cond = hide_in_width
}

local mode = {
	"mode",
	fmt = function(str)
		--return "" .. str .. ""
    	return str:sub(1,1)
	end,
}

local filetype = {
	"filetype",
	icons_enabled = true,
	icon = nil,
    colored = true,
    icon_only = true,
	padding = 1
}
local filename = {
	"filename",
	file_status = true,      -- Displays file status (readonly status, modified status)
    path = 4,                -- 0: Just the filename
                               -- 1: Relative path
                               -- 2: Absolute path
    shorting_target = 40,    -- Shortens path to leave 40 spaces in the window
                               -- for other components. (terrible name, any suggestions?)
    symbols = {
    	modified = '  ',      -- Text to show when the file is modified.
        readonly = '[-]',      -- Text to show when the file is non-modifiable or readonly.
        unnamed = '[No Name]', -- Text to show for unnamed buffers.
	},
	--padding = 0
}


local branch = {
	"branch",
	icons_enabled = true,
	icon = "",
}

local location = {
	"location",
	padding = 0,
}

local buffers = {
	'buffers',
	max_length = 1,
	mode = 0
}

local spaces = function()
	return "spaces: " .. vim.api.nvim_buf_get_option(0, "shiftwidth")
end


lualine.setup({
	options = {
		icons_enabled = true,
		section_separators = { left = "", right = "" },
		disabled_filetypes = { "alpha", "dashboard", "NvimTree", "Outline", "terminal" },
		always_divide_middle = true,
	},
	sections = {
		lualine_a = { mode },    --{ branch, diagnostics },
		lualine_b = {  },     --{ mode },
		lualine_c = {filename, diagnostics, branch,diff},
		-- lualine_x = { "encoding", "fileformat", "filetype" },
		lualine_x = { "filetype"},
		lualine_y = {},     --{ location },
		lualine_z = {},     --{ progress },
	},
	inactive_sections = {
		lualine_a = {},
		lualine_b = {},
		lualine_c = { "filename" },
		lualine_x = { "location" },
		lualine_y = {},
		lualine_z = {},
	},
	tabline = {},
    extension = { {sections = { lualine_b = { "filetype"} }, filetype = { "NvimTree"} } }
})
