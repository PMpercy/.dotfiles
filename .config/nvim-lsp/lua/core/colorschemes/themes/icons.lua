local status_ok, devicons = pcall(require, 'nvim-web-devicons')
if not status_ok then
    return
end

devicons.set_icon {
--require("nvim-web-devicons").set_icon {
    lua = {
        icon = " ",
        color = "#42a5f5",
        cterm_color = "65",
        name = "Lua"
    },
    python = {
        icon = " ",
        color = "#3c78aa",
        cterm_color = "61",
        name = "Py"
    },
    css = {
        icon = " ",
        color = "#42a5f5",
        cterm_color = "60",
        name = "Css"
    },
    html = {
        icon = " ",
        color = "#e44d26",
        cterm_color = "166",
        name = "Html"
    },
    js = {
        icon = " ",
        color = "#ffca28",
        cterm_color = "185",
        name = "Js"
    },
    json = {
        --icon =  "ﬥ  ",
        icon = " ",
        color = "#fbc02d",
        cterm_color = "185",
        name = "Json"
    },
    vim = {
        icon = " ",
        color = "#43a047",
        cterm_color = "29",
        name = "Vim",
    },
    xml = {
        icon = " ",
        color = "#e37933",
        cterm_color = "173",
        name = "Xml",
    },
    scss = {
        icon = "ﳪ ",
        color = "#f55385",
        cterm_color = "204",
        name = "Scss",
    },
}
