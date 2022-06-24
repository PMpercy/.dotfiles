--var global
g = vim.g
opt = vim.opt
cmd = vim.cmd


local core_module = {
	"core",
	"plugins"
}

for _, module in ipairs(core_module) do
	local ok, err = pcall(require, module)
	if not ok then
		print(err)
	end
end


cmd [[ 
    au BufNewFile,BufRead /*.rasi setf css
]]
