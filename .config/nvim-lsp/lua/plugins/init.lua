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


	-- Colorschemes
	use 'marko-cerovac/material.nvim'
	use 'olimorris/onedarkpro.nvim'
    use 'tiagovla/tokyodark.nvim'

	-- cmp plugins
	use "hrsh7th/nvim-cmp" -- The completion plugin
	use "hrsh7th/cmp-buffer" -- buffer completions
	use "hrsh7th/cmp-path" -- path completions
	use "hrsh7th/cmp-cmdline" -- cmdline completions
	use "saadparwaiz1/cmp_luasnip" -- snippet completions
	use "hrsh7th/cmp-nvim-lsp"

	-- snippets
	use "L3MON4D3/LuaSnip" --snippet engine
	use "rafamadriz/friendly-snippets" -- a bunch of snippets to use
	use("onsails/lspkind-nvim") --> vscode-like pictograms for neovim lsp completion items

	-- Automatically set up your configuration after cloning packer.nvim
	-- Put this at the end after all plugins

	--Lsp Server
	use 'neovim/nvim-lspconfig'
	use 'williamboman/nvim-lsp-installer'
	use("jose-elias-alvarez/null-ls.nvim") --> inject lsp diagnistocs, formattings, code actions, and more ...
	use("tami5/lspsaga.nvim") --> icons for LSP diagnostics

	--> treesitter & treesitter modules/plugins
	use { "nvim-treesitter/nvim-treesitter" } --> treesitter


	-- Telescope
	use "nvim-telescope/telescope.nvim"

    use "JoosepAlviste/nvim-ts-context-commentstring"

	-- Git
	--use "lewis6991/gitsigns.nvim"


	if PACKER_BOOTSTRAP then
		require("packer").sync()
	end
end)


