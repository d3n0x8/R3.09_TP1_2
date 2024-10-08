# TP 1+2

## Exercice 1 : Chiffre de Vigenère

### Test 1 :

- Input : texte: `bonjour`, clé: `CLE`
- Output : `&<4.<;6`

### Test 2 :

- Input : texte: `je suis en informatique`, clé: `iut`
- Output : `p8AtI/:R7oS)/46!F5<:'`

### Test 3 :

- Input : texte: `J'ai 19 ans. Nous sommes en 10/2024.`, clé: `bUT._INfo`
- Output : ```-\6w_ZgfQQIb..9DZoVEB{E=NL^bfd=qY`z}```

## Exercice 2 : Déchiffrement du chiffre de Vigenère

### Test 1 :

- Input : texte: `&<4.<;6`,  clé: `CLE`
- Output : `bonjour`

### Test 2 :

- Input : texte: `p8AtI/:R7oS)/46!F5<:'`, clé: `iut`
- Output : `je suis en informatique`

### Test 3 :

- Input : texte: ```-\6w_ZgfQQIb..9DZoVEB{E=NL^bfd=qY`z}```, clé: `bUT._INfo`
- Output : `J'ai 19 ans. Nous sommes en 10/2024.`

## Exercice 3 : L'attaque de Kasiski

### Test 1:

- Input : fichier: `texteTD.txt`, (chiffré avec la clé "PARADIGM")
- Output : `8`

### Test 1:
- Input : fichier: `texte3000.txt`, (chiffré avec la clé "testcle")
- Output : `7`


texteTD.txt:
```
SBGZPLPSLAOZRLLDHAZTTSKUGGURHIUEFPGZCECAWBGOZSKHDBJACOKTDZMQIWVANVKEHEJIQBNQRRPPWWMDPPYIFIRSDRZTKUYFWEDSHTBQHBLTLVYFTAUEAXRAXTNEDSTQHSVSLVZTTIIIPXRQBEETDBOACEMEQBNAJGYTKMMAPLYAVJKQCTYEVISQIHVMHBNASSRNGBKOWNZQXMYAUCIYSBGZPLPSLANMKETHDVMQSDIAVBOOPLCYWPXAJGYTKMNUHTFRBWLOGYGTROXMEHPAGIVFXNXTRQTOGERSLVMOGYGTROXMEHZCFWSBAEOIWGXMCGZNJNXABTYESMTMCDGASMXYTTYOGAURIHVPDAZFWRFUJPSMRHZNHARUZEKHHJXUIIJHEWSNTSRNGKUXDSJUVKUYEUKEUAGFQLVTFPRQNPRRNQTIDRCDZIXUXTFTKMSMIHVMDBOOPLCYDLBMCCVDFWSBJTVRLHKPHCYEPMYAUTYESZKETNKMHBNASSWOUJXQPKZNJUUPTRECUGVFDSPSWMSEDFKEQQTHDLMEVWRHXNXCDZKRJLCYFWTEIRLCWMJBGOSLHUYUCPLRHUGFWEDAWQIEIHVBHAZWCONNEMOZVIETHOKDUATTRZOLPTZOQXNRDGQZUDNKOPIZTTMRTLKGXPNRLBAOEDFTRBXZAVRRPKQIMAGFRLBNYHCIY
```


texte3000.txt:
```
t*UcWl[ce[gE[JtXcnEbSZedZVQ[tJUcWl[ce\dVV`dTsaSVTiG]cccOkG]icbTtPYjRRe\GfXS[eY[scSZeYKsBMYU#eA^P\eV\U^XlZd[^dY_YtXYkIlJV\YcXbXZYsYIlSnYhZVRYtKhtHUOhZc^VRYtGsgEPUcZYgql;ce^dY_eVRcgWlWjO`tJYGcG]icQGcYsjRl\^KimcOGoGftMYeYKWdYcX^ZsjRReXGfiIlGcI]ZR[KtPUjRVKtVUgcYKtZYbT`ef[]tQRTiOccRNOieiccaXZYcgcPGXNYtEbeXUYjVlJjTYtJ\XZZsZRPNVThZIze>ThgMT[ZeA^P\eYKW^HNeYKseE_Z^XsVcYGtXYXLRXXNYtHReXKsiVRYdXsaITKcJU^VRst/`tT_KeGfVcbTtYUXcN\ZIsYIlRZGitHbeeG]ccRZt[bZcOUjYgdPReV\UcXlJZeejMaZZXshS[ekO`aETKtGitPR\ZXsYYlPd[f#c.RdXgtUbOaeaVVPNVOhtPNeWX]hIlLgG]XLRe_UiVMaeYGbhc`KheW]IcKj^sZXlRZYsXLNTiYsYI`edOgZEb^tRUXG\SeG[cEVKcZ"t%]XZYsePbY^KigWlNZ[fZWlOaeUgVV\VeUtP\XZKsYIlRVeZdVRZtUitPRYtGfWVRYtOabI[YZYshIZHaG]ZRaeXNiXL\ZZXsYI`ehKWgIaYtUiWPVKhssAEVXtKhVMaeXNUgKReY[btTNX[[atJYUgG`tI[OkXUcXlKieXZWlXV_ccWlJZe`jQVKgKs[MYZgG]ZRaeVehgEcKgYsaIlLZ[]aPNMZss:RlGkGbXE[ZtVfjHRSbKbic:OaUshIlS^ZsVcR^eRcgI_eXKhtI[JgU]icZG\OejIze>RsgIZGgWiVcQKheZaIbXheUj\lId[`ZY_Yt\]kI`eYKgtG_KVZigI`eX[f^IbYZYsZXlSZSYtY[eg[]hWRGjeejMlYXObiMYRVOhtW\[he`Zc`UaK]aql:d[htElId[dtY[eWXi^XlYd[fYc_KiKbiMaeYKfgMRXZe`jMzeEUihWNTieicc`UjV]gcQGc^]ZXRe^RshIlXZZcjV[GtVcjVlJZIcjZ_OgeiccTXVTXtLVHd[seI_I]KshY_ejTYtF_GcI\Zql:jeW]I_I]KgtY[eiXYhS_eeKh^XlJZSUcHNealc^WRGjeXjRRekU]mcTXV\Y#c<[^e^Zc`[^YsVcYGtXYXLRXXNYtHRef[YaUbKtI\dWReYKshTRI^G`tVRVdTX^Xl3^RctPReXUYjVlHVZhVRast9]tXbekKimcaXd[jZVlIZehgI`UgehjcQKkXUhc_KhUiYVReiXc^WlKcO[bI`eYKWaE_GtRYtLVHd[sfYVehKaWPNOieYiVReaKs\E_J^KbtHReaGs[S_Kiss>RaX^MiZc:OaUsVG^[^KgXEzeAN]WSbeeUgVcYGtVfZQVKgKsZRVMbKs/c>[{KgicPKtWi^cRYie`ZKRXtIcbQRejTYtTY[bKsbEVYtWiZc[[aebZc]KjZsiI[Oge3t%]XZYsjRlSdSYcXlJZefZJYKmOccc:OaUshjR^XRUbEl t)zZWaeaKshSbL[RYtdl2]OVdYlNdI\VcYGtZYiIlYVZ]hJNOissAElYZIccHReZT]\QReZZU^XlVa[gtHVL[OW^PRe/eEjjRYieWZc^[^eWdQZKcIYtTNXt[bt8lL^T]ic]GgeiccAeZZsXS[Z^KbicQ[t:s4c:OaUseI[YVThtEb^tSciWlXZVccHVZt s8jRYieicIlZ]K]ZVReue@]MOUjeUbY`KtRi^cNIXUfYElYVeWdRSOVTWZql6d[ftPNeYKfcMRXZeYcMTSZe`ZcUOWUitHRIaGfVc'eF[zZWaeXKsfYVe\XUcHVZtWiVRQedTsaIlVVXhVKRe4eA^P\eeKfePR^ZedgMaehUbtXRSeYseYVYtYcjHNOceWdQ]X^Zs/c0lZYhtPNe_U]Zcme6\YXcbTtIf^cQKtPc^IlRZe\^F\[tRi^cNTcUbXElWjl]acN\VOhtVR[hY]#cA[tGgtT_Uj\YtXNekG`ZY_eeKh^XlZjedZYeebG]cXRTVThtG\TiObjI_eiGsfYRZZssGIPUcTU^W`GcZsBMYUtXYbI_I^GsaLVHd[sVZNTieXZc_KeXYcH_KtYcccPNZS]cql/aegZRSUcIUtTY[hedgSSUcJYbI[ZtJUcWlRVeZdVRZtYcccPUZ[ftTYK^TsYjRYeU]gql,^TUaIZKcZsVT_KheUkSVXtZfVZRXhKsYI`eW[]hW\TheYeEVYtKhtG\TiUigRReYKgtV\I]KfhcVRtGfgMcGtJUcWl[cKsXPNOgOYgIze6[sXI[ZgKsjRReVTW^I[TZefjM[KtYYtH_KhYU^XlSVPYhXbKjYYbI[ZtGjZGlJZYseMRXgKgtG\[kKfiI`eYKsbSbYhK"t%behUabIaejTsZGYGieXdVReVZh^VNOiegdRlGiZYcXVUcss>PlYVVdgSPNVeUkIPeeXYXEbeiOcccRZtJYXSb\gOhtY[eXUZ[VReZTsWSVYtUfcIlJZeadXVLheXZPVIVZg#cAXZSVaE[ZtJzZ\POiGh^S[e^RsdYcX^ZsaIlIdLZgIlKiemtX_Uj\UtY[eVTW^I[eVXhZJNIiegXM[Z^R`VRaehUihcYGtRibMRXZeXjcWUjX"t1VRdegjXlGtIYicVThZUcXlWjO`tEcG^ZsYIPUj\YgXlH^KbtTY[heejY[ehOaePReiXYhS_st/`tEcG^Zs\ETTZeYcc`G\KghIlKceWdY_G\KsZXlKceUbMaOZeUkIPeaGs[S_Kiss6ZRItRYtG\KjXsaITKge]ac]X^ZsaIlI]Ka^RlJjefZX\[gedgIaeVedVVaG\KftWRYtTcjZRRaKgtLVYiU]gI`eZZsVZRTi[fZWlGkKWtGR[meejMlRV[hdQ]GiOYcXlJVTgtW\Tt\]aPNMZssHS[ekUmVKRea[]tEcG^ZsVT]X^YsfYReaGskI_OiGVaIlX^I\ZW`KtTYtVRY^JU^XlVVYsYE[YtRcgcZG^YsYE[YtRYhcYKXUbhcNVeX]hI`eZZsaI`ehUikI[OgYsXVRKhss6M[Y^e]ac_KiUigRNeXNYocY[^e`Zc`UjX]gIlGj^saIcXZYseVRZtGsgEPUcZYgc`KhedZVVVZZ]ZWlGtZcjWlIZ[ltUbOtRYXSbZZXU^I[Z#
```
