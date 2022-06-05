
--[onedark, tokyonight, dracula, material, nord, onedarkpro, catppuccin, github]
local themes = "onedarkpro"

-- OneDarkPro
if themes == "onedarkpro" then
   	require('core.colorschemes.themes.onedarkpro')
    local onedarkpro = require('core.colorschemes.lualine.onedarkpro')
    require('lualine').setup({
        options = {
            theme = onedarkpro
        }
    })

-- Material
elseif themes == "material" then
	require('core.colorschemes.themes.material')
    local material = require('core.colorschemes.lualine.material')
    local status_ok, lualine = pcall(require, 'lualine')
    if not status_ok then
        return
    end
    lualine.setup({
        options = {
            theme = material
        }
    })

end

--return themes

