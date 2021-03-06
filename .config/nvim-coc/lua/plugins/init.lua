require 'plugins.configs'

local fn = vim.fn

-- Automatically install packer
local install_path = fn.stdpath "data" .. "/site/pack/packer/start/packer.nvim"
if fn.empty(fn.glob(install_path)) > 0 then
PACKER_BOOTSTRAP = fn.system {
    "git",
    "clone",
    "--depth",
    "1",
    "https://github.com/wbthomason/packer.nvim",
    install_path,
}
print "Installing packer close and reopen Neovim..."
vim.cmd [[packadd packer.nvim]]
end

-- Autocommand that reloads neovim whenever you save the plugins.lua file
--vim.cmd [[
--augroup packer_user_config
--    autocmd!
--    autocmd BufWritePost init.lua source <afile> | PackerSync
--augroup end
--]]

-- Use a protected call so we don't error out on first use
local status_ok, packer = pcall(require, "packer")
if not status_ok then
return
end

-- Have packer use a popup window
packer.init {
display = {
    open_fn = function()
    return require("packer.util").float { border = "single" }
    end,
},
}

-- Install your plugins here
return packer.startup(function(use)

	use "wbthomason/packer.nvim" -- Have packer manage itself
	use "nvim-lua/popup.nvim" -- An implementation of the Popup API from vim in Neovim
	use "nvim-lua/plenary.nvim" -- Useful lua functions used ny lots of plugins
	use "windwp/nvim-autopairs" -- Autopairs, integrates with both cmp and treesitter
	use "numToStr/Comment.nvim" -- Easily comment stuff
	use "kyazdani42/nvim-web-devicons"
	use "kyazdani42/nvim-tree.lua"
	use "nvim-lualine/lualine.nvim"
	use "lukas-reineke/indent-blankline.nvim"
	use "folke/which-key.nvim"
	use 'norcalli/nvim-colorizer.lua'
    use 'kosayoda/nvim-lightbulb'

	-- Colorschemes
	use 'marko-cerovac/material.nvim'
	use 'olimorris/onedarkpro.nvim'
    use 'tiagovla/tokyodark.nvim'

	--coc
    use {'neoclide/coc.nvim', branch = 'release'}

	--> treesitter & treesitter modules/plugins
	use { "nvim-treesitter/nvim-treesitter" } --> treesitter


	-- Telescope
	use "nvim-telescope/telescope.nvim"

	--use "lewis6991/gitsigns.nvim"


	if PACKER_BOOTSTRAP then
		require("packer").sync()
	end
end)


