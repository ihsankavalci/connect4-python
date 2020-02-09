Connect-4 Game with Q-Learning Algorithm

Created by @karakusfurkan and @ihsankavalci and done as a graduation project.

Q-Learning
Q-learning is a model-free reinforcement learning algorithm. The goal of Q-learning is to learn a policy, which tells an agent what action to take under what circumstances. It does not require a model (hence the connotation "model-free") of the environment, and it can handle problems with stochastic transitions and rewards, without requiring adaptations.

<svg xmlns:xlink="http://www.w3.org/1999/xlink" width="96.268ex" height="16.843ex" style="vertical-align: -9.671ex; margin-right: -0.028ex;" viewBox="0 -3087.6 41448.4 7251.7" role="img" focusable="false" xmlns="http://www.w3.org/2000/svg" aria-labelledby="MathJax-SVG-1-Title">
<title id="MathJax-SVG-1-Title">{\displaystyle Q^{new}(s_{t},a_{t})\leftarrow \underbrace {Q(s_{t},a_{t})} _{\text{old value}}+\underbrace {\alpha } _{\text{learning rate}}\cdot \overbrace {{\bigg (}\underbrace {\underbrace {r_{t}} _{\text{reward}}+\underbrace {\gamma } _{\text{discount factor}}\cdot \underbrace {\max _{a}Q(s_{t+1},a)} _{\text{estimate of optimal future value}}} _{\text{new value (temporal difference target)}}-\underbrace {Q(s_{t},a_{t})} _{\text{old value}}{\bigg )}} ^{\text{temporal difference}}}</title>
<defs aria-hidden="true">
<path stroke-width="1" id="E1-MJMATHI-51" d="M399 -80Q399 -47 400 -30T402 -11V-7L387 -11Q341 -22 303 -22Q208 -22 138 35T51 201Q50 209 50 244Q50 346 98 438T227 601Q351 704 476 704Q514 704 524 703Q621 689 680 617T740 435Q740 255 592 107Q529 47 461 16L444 8V3Q444 2 449 -24T470 -66T516 -82Q551 -82 583 -60T625 -3Q631 11 638 11Q647 11 649 2Q649 -6 639 -34T611 -100T557 -165T481 -194Q399 -194 399 -87V-80ZM636 468Q636 523 621 564T580 625T530 655T477 665Q429 665 379 640Q277 591 215 464T153 216Q153 110 207 59Q231 38 236 38V46Q236 86 269 120T347 155Q372 155 390 144T417 114T429 82T435 55L448 64Q512 108 557 185T619 334T636 468ZM314 18Q362 18 404 39L403 49Q399 104 366 115Q354 117 347 117Q344 117 341 117T337 118Q317 118 296 98T274 52Q274 18 314 18Z"></path>
<path stroke-width="1" id="E1-MJMATHI-6E" d="M21 287Q22 293 24 303T36 341T56 388T89 425T135 442Q171 442 195 424T225 390T231 369Q231 367 232 367L243 378Q304 442 382 442Q436 442 469 415T503 336T465 179T427 52Q427 26 444 26Q450 26 453 27Q482 32 505 65T540 145Q542 153 560 153Q580 153 580 145Q580 144 576 130Q568 101 554 73T508 17T439 -10Q392 -10 371 17T350 73Q350 92 386 193T423 345Q423 404 379 404H374Q288 404 229 303L222 291L189 157Q156 26 151 16Q138 -11 108 -11Q95 -11 87 -5T76 7T74 17Q74 30 112 180T152 343Q153 348 153 366Q153 405 129 405Q91 405 66 305Q60 285 60 284Q58 278 41 278H27Q21 284 21 287Z"></path>
<path stroke-width="1" id="E1-MJMATHI-65" d="M39 168Q39 225 58 272T107 350T174 402T244 433T307 442H310Q355 442 388 420T421 355Q421 265 310 237Q261 224 176 223Q139 223 138 221Q138 219 132 186T125 128Q125 81 146 54T209 26T302 45T394 111Q403 121 406 121Q410 121 419 112T429 98T420 82T390 55T344 24T281 -1T205 -11Q126 -11 83 42T39 168ZM373 353Q367 405 305 405Q272 405 244 391T199 357T170 316T154 280T149 261Q149 260 169 260Q282 260 327 284T373 353Z"></path>
<path stroke-width="1" id="E1-MJMATHI-77" d="M580 385Q580 406 599 424T641 443Q659 443 674 425T690 368Q690 339 671 253Q656 197 644 161T609 80T554 12T482 -11Q438 -11 404 5T355 48Q354 47 352 44Q311 -11 252 -11Q226 -11 202 -5T155 14T118 53T104 116Q104 170 138 262T173 379Q173 380 173 381Q173 390 173 393T169 400T158 404H154Q131 404 112 385T82 344T65 302T57 280Q55 278 41 278H27Q21 284 21 287Q21 293 29 315T52 366T96 418T161 441Q204 441 227 416T250 358Q250 340 217 250T184 111Q184 65 205 46T258 26Q301 26 334 87L339 96V119Q339 122 339 128T340 136T341 143T342 152T345 165T348 182T354 206T362 238T373 281Q402 395 406 404Q419 431 449 431Q468 431 475 421T483 402Q483 389 454 274T422 142Q420 131 420 107V100Q420 85 423 71T442 42T487 26Q558 26 600 148Q609 171 620 213T632 273Q632 306 619 325T593 357T580 385Z"></path>
<path stroke-width="1" id="E1-MJMAIN-28" d="M94 250Q94 319 104 381T127 488T164 576T202 643T244 695T277 729T302 750H315H319Q333 750 333 741Q333 738 316 720T275 667T226 581T184 443T167 250T184 58T225 -81T274 -167T316 -220T333 -241Q333 -250 318 -250H315H302L274 -226Q180 -141 137 -14T94 250Z"></path>
<path stroke-width="1" id="E1-MJMATHI-73" d="M131 289Q131 321 147 354T203 415T300 442Q362 442 390 415T419 355Q419 323 402 308T364 292Q351 292 340 300T328 326Q328 342 337 354T354 372T367 378Q368 378 368 379Q368 382 361 388T336 399T297 405Q249 405 227 379T204 326Q204 301 223 291T278 274T330 259Q396 230 396 163Q396 135 385 107T352 51T289 7T195 -10Q118 -10 86 19T53 87Q53 126 74 143T118 160Q133 160 146 151T160 120Q160 94 142 76T111 58Q109 57 108 57T107 55Q108 52 115 47T146 34T201 27Q237 27 263 38T301 66T318 97T323 122Q323 150 302 164T254 181T195 196T148 231Q131 256 131 289Z"></path>
<path stroke-width="1" id="E1-MJMATHI-74" d="M26 385Q19 392 19 395Q19 399 22 411T27 425Q29 430 36 430T87 431H140L159 511Q162 522 166 540T173 566T179 586T187 603T197 615T211 624T229 626Q247 625 254 615T261 596Q261 589 252 549T232 470L222 433Q222 431 272 431H323Q330 424 330 420Q330 398 317 385H210L174 240Q135 80 135 68Q135 26 162 26Q197 26 230 60T283 144Q285 150 288 151T303 153H307Q322 153 322 145Q322 142 319 133Q314 117 301 95T267 48T216 6T155 -11Q125 -11 98 4T59 56Q57 64 57 83V101L92 241Q127 382 128 383Q128 385 77 385H26Z"></path>
<path stroke-width="1" id="E1-MJMAIN-2C" d="M78 35T78 60T94 103T137 121Q165 121 187 96T210 8Q210 -27 201 -60T180 -117T154 -158T130 -185T117 -194Q113 -194 104 -185T95 -172Q95 -168 106 -156T131 -126T157 -76T173 -3V9L172 8Q170 7 167 6T161 3T152 1T140 0Q113 0 96 17Z"></path>
<path stroke-width="1" id="E1-MJMATHI-61" d="M33 157Q33 258 109 349T280 441Q331 441 370 392Q386 422 416 422Q429 422 439 414T449 394Q449 381 412 234T374 68Q374 43 381 35T402 26Q411 27 422 35Q443 55 463 131Q469 151 473 152Q475 153 483 153H487Q506 153 506 144Q506 138 501 117T481 63T449 13Q436 0 417 -8Q409 -10 393 -10Q359 -10 336 5T306 36L300 51Q299 52 296 50Q294 48 292 46Q233 -10 172 -10Q117 -10 75 30T33 157ZM351 328Q351 334 346 350T323 385T277 405Q242 405 210 374T160 293Q131 214 119 129Q119 126 119 118T118 106Q118 61 136 44T179 26Q217 26 254 59T298 110Q300 114 325 217T351 328Z"></path>
<path stroke-width="1" id="E1-MJMAIN-29" d="M60 749L64 750Q69 750 74 750H86L114 726Q208 641 251 514T294 250Q294 182 284 119T261 12T224 -76T186 -143T145 -194T113 -227T90 -246Q87 -249 86 -250H74Q66 -250 63 -250T58 -247T55 -238Q56 -237 66 -225Q221 -64 221 250T66 725Q56 737 55 738Q55 746 60 749Z"></path>
<path stroke-width="1" id="E1-MJMAIN-2190" d="M944 261T944 250T929 230H165Q167 228 182 216T211 189T244 152T277 96T303 25Q308 7 308 0Q308 -11 288 -11Q281 -11 278 -11T272 -7T267 2T263 21Q245 94 195 151T73 236Q58 242 55 247Q55 254 59 257T73 264Q121 283 158 314T215 375T247 434T264 480L267 497Q269 503 270 505T275 509T288 511Q308 511 308 500Q308 493 303 475Q293 438 278 406T246 352T215 315T185 287T165 270H929Q944 261 944 250Z"></path>
<path stroke-width="1" id="E1-MJSZ4-E152" d="M-24 327L-18 333H-1Q11 333 15 333T22 329T27 322T35 308T54 284Q115 203 225 162T441 120Q454 120 457 117T460 95V60V28Q460 8 457 4T442 0Q355 0 260 36Q75 118 -16 278L-24 292V327Z"></path>
<path stroke-width="1" id="E1-MJSZ4-E153" d="M-10 60V95Q-10 113 -7 116T9 120Q151 120 250 171T396 284Q404 293 412 305T424 324T431 331Q433 333 451 333H468L474 327V292L466 278Q375 118 190 36Q95 0 8 0Q-5 0 -7 3T-10 24V60Z"></path>
<path stroke-width="1" id="E1-MJSZ4-E151" d="M-10 60Q-10 104 -10 111T-5 118Q-1 120 10 120Q96 120 190 84Q375 2 466 -158L474 -172V-207L468 -213H451H447Q437 -213 434 -213T428 -209T423 -202T414 -187T396 -163Q331 -82 224 -41T9 0Q-4 0 -7 3T-10 25V60Z"></path>
<path stroke-width="1" id="E1-MJSZ4-E150" d="M-18 -213L-24 -207V-172L-16 -158Q75 2 260 84Q334 113 415 119Q418 119 427 119T440 120Q454 120 457 117T460 98V60V25Q460 7 457 4T441 0Q308 0 193 -55T25 -205Q21 -211 18 -212T-1 -213H-18Z"></path>
<path stroke-width="1" id="E1-MJSZ4-E154" d="M-10 0V120H410V0H-10Z"></path>
<path stroke-width="1" id="E1-MJMAIN-6F" d="M28 214Q28 309 93 378T250 448Q340 448 405 380T471 215Q471 120 407 55T250 -10Q153 -10 91 57T28 214ZM250 30Q372 30 372 193V225V250Q372 272 371 288T364 326T348 362T317 390T268 410Q263 411 252 411Q222 411 195 399Q152 377 139 338T126 246V226Q126 130 145 91Q177 30 250 30Z"></path>
<path stroke-width="1" id="E1-MJMAIN-6C" d="M42 46H56Q95 46 103 60V68Q103 77 103 91T103 124T104 167T104 217T104 272T104 329Q104 366 104 407T104 482T104 542T103 586T103 603Q100 622 89 628T44 637H26V660Q26 683 28 683L38 684Q48 685 67 686T104 688Q121 689 141 690T171 693T182 694H185V379Q185 62 186 60Q190 52 198 49Q219 46 247 46H263V0H255L232 1Q209 2 183 2T145 3T107 3T57 1L34 0H26V46H42Z"></path>
<path stroke-width="1" id="E1-MJMAIN-64" d="M376 495Q376 511 376 535T377 568Q377 613 367 624T316 637H298V660Q298 683 300 683L310 684Q320 685 339 686T376 688Q393 689 413 690T443 693T454 694H457V390Q457 84 458 81Q461 61 472 55T517 46H535V0Q533 0 459 -5T380 -11H373V44L365 37Q307 -11 235 -11Q158 -11 96 50T34 215Q34 315 97 378T244 442Q319 442 376 393V495ZM373 342Q328 405 260 405Q211 405 173 369Q146 341 139 305T131 211Q131 155 138 120T173 59Q203 26 251 26Q322 26 373 103V342Z"></path>
<path stroke-width="1" id="E1-MJMAIN-76" d="M338 431Q344 429 422 429Q479 429 503 431H508V385H497Q439 381 423 345Q421 341 356 172T288 -2Q283 -11 263 -11Q244 -11 239 -2Q99 359 98 364Q93 378 82 381T43 385H19V431H25L33 430Q41 430 53 430T79 430T104 429T122 428Q217 428 232 431H240V385H226Q187 384 184 370Q184 366 235 234L286 102L377 341V349Q377 363 367 372T349 383T335 385H331V431H338Z"></path>
<path stroke-width="1" id="E1-MJMAIN-61" d="M137 305T115 305T78 320T63 359Q63 394 97 421T218 448Q291 448 336 416T396 340Q401 326 401 309T402 194V124Q402 76 407 58T428 40Q443 40 448 56T453 109V145H493V106Q492 66 490 59Q481 29 455 12T400 -6T353 12T329 54V58L327 55Q325 52 322 49T314 40T302 29T287 17T269 6T247 -2T221 -8T190 -11Q130 -11 82 20T34 107Q34 128 41 147T68 188T116 225T194 253T304 268H318V290Q318 324 312 340Q290 411 215 411Q197 411 181 410T156 406T148 403Q170 388 170 359Q170 334 154 320ZM126 106Q126 75 150 51T209 26Q247 26 276 49T315 109Q317 116 318 175Q318 233 317 233Q309 233 296 232T251 223T193 203T147 166T126 106Z"></path>
<path stroke-width="1" id="E1-MJMAIN-75" d="M383 58Q327 -10 256 -10H249Q124 -10 105 89Q104 96 103 226Q102 335 102 348T96 369Q86 385 36 385H25V408Q25 431 27 431L38 432Q48 433 67 434T105 436Q122 437 142 438T172 441T184 442H187V261Q188 77 190 64Q193 49 204 40Q224 26 264 26Q290 26 311 35T343 58T363 90T375 120T379 144Q379 145 379 161T380 201T380 248V315Q380 361 370 372T320 385H302V431Q304 431 378 436T457 442H464V264Q464 84 465 81Q468 61 479 55T524 46H542V0Q540 0 467 -5T390 -11H383V58Z"></path>
<path stroke-width="1" id="E1-MJMAIN-65" d="M28 218Q28 273 48 318T98 391T163 433T229 448Q282 448 320 430T378 380T406 316T415 245Q415 238 408 231H126V216Q126 68 226 36Q246 30 270 30Q312 30 342 62Q359 79 369 104L379 128Q382 131 395 131H398Q415 131 415 121Q415 117 412 108Q393 53 349 21T250 -11Q155 -11 92 58T28 218ZM333 275Q322 403 238 411H236Q228 411 220 410T195 402T166 381T143 340T127 274V267H333V275Z"></path>
<path stroke-width="1" id="E1-MJMAIN-2B" d="M56 237T56 250T70 270H369V420L370 570Q380 583 389 583Q402 583 409 568V270H707Q722 262 722 250T707 230H409V-68Q401 -82 391 -82H389H387Q375 -82 369 -68V230H70Q56 237 56 250Z"></path>
<path stroke-width="1" id="E1-MJMATHI-3B1" d="M34 156Q34 270 120 356T309 442Q379 442 421 402T478 304Q484 275 485 237V208Q534 282 560 374Q564 388 566 390T582 393Q603 393 603 385Q603 376 594 346T558 261T497 161L486 147L487 123Q489 67 495 47T514 26Q528 28 540 37T557 60Q559 67 562 68T577 70Q597 70 597 62Q597 56 591 43Q579 19 556 5T512 -10H505Q438 -10 414 62L411 69L400 61Q390 53 370 41T325 18T267 -2T203 -11Q124 -11 79 39T34 156ZM208 26Q257 26 306 47T379 90L403 112Q401 255 396 290Q382 405 304 405Q235 405 183 332Q156 292 139 224T121 120Q121 71 146 49T208 26Z"></path>
<path stroke-width="1" id="E1-MJMAIN-72" d="M36 46H50Q89 46 97 60V68Q97 77 97 91T98 122T98 161T98 203Q98 234 98 269T98 328L97 351Q94 370 83 376T38 385H20V408Q20 431 22 431L32 432Q42 433 60 434T96 436Q112 437 131 438T160 441T171 442H174V373Q213 441 271 441H277Q322 441 343 419T364 373Q364 352 351 337T313 322Q288 322 276 338T263 372Q263 381 265 388T270 400T273 405Q271 407 250 401Q234 393 226 386Q179 341 179 207V154Q179 141 179 127T179 101T180 81T180 66V61Q181 59 183 57T188 54T193 51T200 49T207 48T216 47T225 47T235 46T245 46H276V0H267Q249 3 140 3Q37 3 28 0H20V46H36Z"></path>
<path stroke-width="1" id="E1-MJMAIN-6E" d="M41 46H55Q94 46 102 60V68Q102 77 102 91T102 122T103 161T103 203Q103 234 103 269T102 328V351Q99 370 88 376T43 385H25V408Q25 431 27 431L37 432Q47 433 65 434T102 436Q119 437 138 438T167 441T178 442H181V402Q181 364 182 364T187 369T199 384T218 402T247 421T285 437Q305 442 336 442Q450 438 463 329Q464 322 464 190V104Q464 66 466 59T477 49Q498 46 526 46H542V0H534L510 1Q487 2 460 2T422 3Q319 3 310 0H302V46H318Q379 46 379 62Q380 64 380 200Q379 335 378 343Q372 371 358 385T334 402T308 404Q263 404 229 370Q202 343 195 315T187 232V168V108Q187 78 188 68T191 55T200 49Q221 46 249 46H265V0H257L234 1Q210 2 183 2T145 3Q42 3 33 0H25V46H41Z"></path>
<path stroke-width="1" id="E1-MJMAIN-69" d="M69 609Q69 637 87 653T131 669Q154 667 171 652T188 609Q188 579 171 564T129 549Q104 549 87 564T69 609ZM247 0Q232 3 143 3Q132 3 106 3T56 1L34 0H26V46H42Q70 46 91 49Q100 53 102 60T104 102V205V293Q104 345 102 359T88 378Q74 385 41 385H30V408Q30 431 32 431L42 432Q52 433 70 434T106 436Q123 437 142 438T171 441T182 442H185V62Q190 52 197 50T232 46H255V0H247Z"></path>
<path stroke-width="1" id="E1-MJMAIN-67" d="M329 409Q373 453 429 453Q459 453 472 434T485 396Q485 382 476 371T449 360Q416 360 412 390Q410 404 415 411Q415 412 416 414V415Q388 412 363 393Q355 388 355 386Q355 385 359 381T368 369T379 351T388 325T392 292Q392 230 343 187T222 143Q172 143 123 171Q112 153 112 133Q112 98 138 81Q147 75 155 75T227 73Q311 72 335 67Q396 58 431 26Q470 -13 470 -72Q470 -139 392 -175Q332 -206 250 -206Q167 -206 107 -175Q29 -140 29 -75Q29 -39 50 -15T92 18L103 24Q67 55 67 108Q67 155 96 193Q52 237 52 292Q52 355 102 398T223 442Q274 442 318 416L329 409ZM299 343Q294 371 273 387T221 404Q192 404 171 388T145 343Q142 326 142 292Q142 248 149 227T179 192Q196 182 222 182Q244 182 260 189T283 207T294 227T299 242Q302 258 302 292T299 343ZM403 -75Q403 -50 389 -34T348 -11T299 -2T245 0H218Q151 0 138 -6Q118 -15 107 -34T95 -74Q95 -84 101 -97T122 -127T170 -155T250 -167Q319 -167 361 -139T403 -75Z"></path>
<path stroke-width="1" id="E1-MJMAIN-74" d="M27 422Q80 426 109 478T141 600V615H181V431H316V385H181V241Q182 116 182 100T189 68Q203 29 238 29Q282 29 292 100Q293 108 293 146V181H333V146V134Q333 57 291 17Q264 -10 221 -10Q187 -10 162 2T124 33T105 68T98 100Q97 107 97 248V385H18V422H27Z"></path>
<path stroke-width="1" id="E1-MJMAIN-22C5" d="M78 250Q78 274 95 292T138 310Q162 310 180 294T199 251Q199 226 182 208T139 190T96 207T78 250Z"></path>
<path stroke-width="1" id="E1-MJSZ3-28" d="M701 -940Q701 -943 695 -949H664Q662 -947 636 -922T591 -879T537 -818T475 -737T412 -636T350 -511T295 -362T250 -186T221 17T209 251Q209 962 573 1361Q596 1386 616 1405T649 1437T664 1450H695Q701 1444 701 1441Q701 1436 681 1415T629 1356T557 1261T476 1118T400 927T340 675T308 359Q306 321 306 250Q306 -139 400 -430T690 -924Q701 -936 701 -940Z"></path>
<path stroke-width="1" id="E1-MJMATHI-72" d="M21 287Q22 290 23 295T28 317T38 348T53 381T73 411T99 433T132 442Q161 442 183 430T214 408T225 388Q227 382 228 382T236 389Q284 441 347 441H350Q398 441 422 400Q430 381 430 363Q430 333 417 315T391 292T366 288Q346 288 334 299T322 328Q322 376 378 392Q356 405 342 405Q286 405 239 331Q229 315 224 298T190 165Q156 25 151 16Q138 -11 108 -11Q95 -11 87 -5T76 7T74 17Q74 30 114 189T154 366Q154 405 128 405Q107 405 92 377T68 316T57 280Q55 278 41 278H27Q21 284 21 287Z"></path>
<path stroke-width="1" id="E1-MJMAIN-77" d="M90 368Q84 378 76 380T40 385H18V431H24L43 430Q62 430 84 429T116 428Q206 428 221 431H229V385H215Q177 383 177 368Q177 367 221 239L265 113L339 328L333 345Q323 374 316 379Q308 384 278 385H258V431H264Q270 428 348 428Q439 428 454 431H461V385H452Q404 385 404 369Q404 366 418 324T449 234T481 143L496 100L537 219Q579 341 579 347Q579 363 564 373T530 385H522V431H529Q541 428 624 428Q692 428 698 431H703V385H697Q696 385 691 385T682 384Q635 377 619 334L559 161Q546 124 528 71Q508 12 503 1T487 -11H479Q460 -11 456 -4Q455 -3 407 133L361 267Q359 263 266 -4Q261 -11 243 -11H238Q225 -11 220 -3L90 368Z"></path>
<path stroke-width="1" id="E1-MJMATHI-3B3" d="M31 249Q11 249 11 258Q11 275 26 304T66 365T129 418T206 441Q233 441 239 440Q287 429 318 386T371 255Q385 195 385 170Q385 166 386 166L398 193Q418 244 443 300T486 391T508 430Q510 431 524 431H537Q543 425 543 422Q543 418 522 378T463 251T391 71Q385 55 378 6T357 -100Q341 -165 330 -190T303 -216Q286 -216 286 -188Q286 -138 340 32L346 51L347 69Q348 79 348 100Q348 257 291 317Q251 355 196 355Q148 355 108 329T51 260Q49 251 47 251Q45 249 31 249Z"></path>
<path stroke-width="1" id="E1-MJMAIN-73" d="M295 316Q295 356 268 385T190 414Q154 414 128 401Q98 382 98 349Q97 344 98 336T114 312T157 287Q175 282 201 278T245 269T277 256Q294 248 310 236T342 195T359 133Q359 71 321 31T198 -10H190Q138 -10 94 26L86 19L77 10Q71 4 65 -1L54 -11H46H42Q39 -11 33 -5V74V132Q33 153 35 157T45 162H54Q66 162 70 158T75 146T82 119T101 77Q136 26 198 26Q295 26 295 104Q295 133 277 151Q257 175 194 187T111 210Q75 227 54 256T33 318Q33 357 50 384T93 424T143 442T187 447H198Q238 447 268 432L283 424L292 431Q302 440 314 448H322H326Q329 448 335 442V310L329 304H301Q295 310 295 316Z"></path>
<path stroke-width="1" id="E1-MJMAIN-63" d="M370 305T349 305T313 320T297 358Q297 381 312 396Q317 401 317 402T307 404Q281 408 258 408Q209 408 178 376Q131 329 131 219Q131 137 162 90Q203 29 272 29Q313 29 338 55T374 117Q376 125 379 127T395 129H409Q415 123 415 120Q415 116 411 104T395 71T366 33T318 2T249 -11Q163 -11 99 53T34 214Q34 318 99 383T250 448T370 421T404 357Q404 334 387 320Z"></path>
<path stroke-width="1" id="E1-MJMAIN-66" d="M273 0Q255 3 146 3Q43 3 34 0H26V46H42Q70 46 91 49Q99 52 103 60Q104 62 104 224V385H33V431H104V497L105 564L107 574Q126 639 171 668T266 704Q267 704 275 704T289 705Q330 702 351 679T372 627Q372 604 358 590T321 576T284 590T270 627Q270 647 288 667H284Q280 668 273 668Q245 668 223 647T189 592Q183 572 182 497V431H293V385H185V225Q185 63 186 61T189 57T194 54T199 51T206 49T213 48T222 47T231 47T241 46T251 46H282V0H273Z"></path>
<path stroke-width="1" id="E1-MJMAIN-6D" d="M41 46H55Q94 46 102 60V68Q102 77 102 91T102 122T103 161T103 203Q103 234 103 269T102 328V351Q99 370 88 376T43 385H25V408Q25 431 27 431L37 432Q47 433 65 434T102 436Q119 437 138 438T167 441T178 442H181V402Q181 364 182 364T187 369T199 384T218 402T247 421T285 437Q305 442 336 442Q351 442 364 440T387 434T406 426T421 417T432 406T441 395T448 384T452 374T455 366L457 361L460 365Q463 369 466 373T475 384T488 397T503 410T523 422T546 432T572 439T603 442Q729 442 740 329Q741 322 741 190V104Q741 66 743 59T754 49Q775 46 803 46H819V0H811L788 1Q764 2 737 2T699 3Q596 3 587 0H579V46H595Q656 46 656 62Q657 64 657 200Q656 335 655 343Q649 371 635 385T611 402T585 404Q540 404 506 370Q479 343 472 315T464 232V168V108Q464 78 465 68T468 55T477 49Q498 46 526 46H542V0H534L510 1Q487 2 460 2T422 3Q319 3 310 0H302V46H318Q379 46 379 62Q380 64 380 200Q379 335 378 343Q372 371 358 385T334 402T308 404Q263 404 229 370Q202 343 195 315T187 232V168V108Q187 78 188 68T191 55T200 49Q221 46 249 46H265V0H257L234 1Q210 2 183 2T145 3Q42 3 33 0H25V46H41Z"></path>
<path stroke-width="1" id="E1-MJMAIN-78" d="M201 0Q189 3 102 3Q26 3 17 0H11V46H25Q48 47 67 52T96 61T121 78T139 96T160 122T180 150L226 210L168 288Q159 301 149 315T133 336T122 351T113 363T107 370T100 376T94 379T88 381T80 383Q74 383 44 385H16V431H23Q59 429 126 429Q219 429 229 431H237V385Q201 381 201 369Q201 367 211 353T239 315T268 274L272 270L297 304Q329 345 329 358Q329 364 327 369T322 376T317 380T310 384L307 385H302V431H309Q324 428 408 428Q487 428 493 431H499V385H492Q443 385 411 368Q394 360 377 341T312 257L296 236L358 151Q424 61 429 57T446 50Q464 46 499 46H516V0H510H502Q494 1 482 1T457 2T432 2T414 3Q403 3 377 3T327 1L304 0H295V46H298Q309 46 320 51T331 63Q331 65 291 120L250 175Q249 174 219 133T185 88Q181 83 181 74Q181 63 188 55T206 46Q208 46 208 23V0H201Z"></path>
<path stroke-width="1" id="E1-MJMAIN-31" d="M213 578L200 573Q186 568 160 563T102 556H83V602H102Q149 604 189 617T245 641T273 663Q275 666 285 666Q294 666 302 660V361L303 61Q310 54 315 52T339 48T401 46H427V0H416Q395 3 257 3Q121 3 100 0H88V46H114Q136 46 152 46T177 47T193 50T201 52T207 57T213 61V578Z"></path>
<path stroke-width="1" id="E1-MJMAIN-70" d="M36 -148H50Q89 -148 97 -134V-126Q97 -119 97 -107T97 -77T98 -38T98 6T98 55T98 106Q98 140 98 177T98 243T98 296T97 335T97 351Q94 370 83 376T38 385H20V408Q20 431 22 431L32 432Q42 433 61 434T98 436Q115 437 135 438T165 441T176 442H179V416L180 390L188 397Q247 441 326 441Q407 441 464 377T522 216Q522 115 457 52T310 -11Q242 -11 190 33L182 40V-45V-101Q182 -128 184 -134T195 -145Q216 -148 244 -148H260V-194H252L228 -193Q205 -192 178 -192T140 -191Q37 -191 28 -194H20V-148H36ZM424 218Q424 292 390 347T305 402Q234 402 182 337V98Q222 26 294 26Q345 26 384 80T424 218Z"></path>
<path stroke-width="1" id="E1-MJMAIN-2212" d="M84 237T84 250T98 270H679Q694 262 694 250T679 230H98Q84 237 84 250Z"></path>
<path stroke-width="1" id="E1-MJSZ3-29" d="M34 1438Q34 1446 37 1448T50 1450H56H71Q73 1448 99 1423T144 1380T198 1319T260 1238T323 1137T385 1013T440 864T485 688T514 485T526 251Q526 134 519 53Q472 -519 162 -860Q139 -885 119 -904T86 -936T71 -949H56Q43 -949 39 -947T34 -937Q88 -883 140 -813Q428 -430 428 251Q428 453 402 628T338 922T245 1146T145 1309T46 1425Q44 1427 42 1429T39 1433T36 1436L34 1438Z"></path>
</defs>
<g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)" aria-hidden="true">
 <use xlink:href="#E1-MJMATHI-51" x="0" y="0"></use>
<g transform="translate(791,412)">
 <use transform="scale(0.707)" xlink:href="#E1-MJMATHI-6E" x="0" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMATHI-65" x="600" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMATHI-77" x="1067" y="0"></use>
</g>
 <use xlink:href="#E1-MJMAIN-28" x="2152" y="0"></use>
<g transform="translate(2542,0)">
 <use xlink:href="#E1-MJMATHI-73" x="0" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMATHI-74" x="663" y="-213"></use>
</g>
 <use xlink:href="#E1-MJMAIN-2C" x="3367" y="0"></use>
<g transform="translate(3812,0)">
 <use xlink:href="#E1-MJMATHI-61" x="0" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMATHI-74" x="748" y="-213"></use>
</g>
 <use xlink:href="#E1-MJMAIN-29" x="4697" y="0"></use>
 <use xlink:href="#E1-MJMAIN-2190" x="5364" y="0"></use>
<g transform="translate(6643,0)">
 <use xlink:href="#E1-MJMATHI-51" x="0" y="0"></use>
 <use xlink:href="#E1-MJMAIN-28" x="791" y="0"></use>
<g transform="translate(1181,0)">
 <use xlink:href="#E1-MJMATHI-73" x="0" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMATHI-74" x="663" y="-213"></use>
</g>
 <use xlink:href="#E1-MJMAIN-2C" x="2006" y="0"></use>
<g transform="translate(2451,0)">
 <use xlink:href="#E1-MJMATHI-61" x="0" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMATHI-74" x="748" y="-213"></use>
</g>
 <use xlink:href="#E1-MJMAIN-29" x="3336" y="0"></use>
<g transform="translate(11,-765)">
 <use xlink:href="#E1-MJSZ4-E152" x="23" y="0"></use>
<g transform="translate(505.0007098332299,0) scale(2.2106010350768335,1)">
 <use xlink:href="#E1-MJSZ4-E154"></use>
</g>
<g transform="translate(1412,0)">
 <use xlink:href="#E1-MJSZ4-E151"></use>
 <use xlink:href="#E1-MJSZ4-E150" x="450" y="0"></use>
</g>
<g transform="translate(2334.4531445655,0) scale(2.2106010350768335,1)">
 <use xlink:href="#E1-MJSZ4-E154"></use>
</g>
 <use xlink:href="#E1-MJSZ4-E153" x="3251" y="0"></use>
</g>
<g transform="translate(449,-1638)">
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-6F"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-6C" x="500" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-64" x="779" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-76" x="1689" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-61" x="2217" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-6C" x="2718" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-75" x="2996" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-65" x="3553" y="0"></use>
</g>
</g>
 <use xlink:href="#E1-MJMAIN-2B" x="10591" y="0"></use>
<g transform="translate(11591,0)">
<g transform="translate(1146,0)">
 <use xlink:href="#E1-MJMATHI-3B1" x="508" y="0"></use>
<g transform="translate(0,-526)">
 <use xlink:href="#E1-MJSZ4-E152" x="23" y="0"></use>
<g transform="translate(390,0)">
 <use xlink:href="#E1-MJSZ4-E151"></use>
 <use xlink:href="#E1-MJSZ4-E150" x="450" y="0"></use>
</g>
 <use xlink:href="#E1-MJSZ4-E153" x="1207" y="0"></use>
</g>
</g>
<g transform="translate(0,-1399)">
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-6C"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-65" x="278" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-61" x="723" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-72" x="1223" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-6E" x="1616" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-69" x="2172" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-6E" x="2451" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-67" x="3007" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-72" x="3861" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-61" x="4254" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-74" x="4754" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-65" x="5144" y="0"></use>
</g>
</g>
 <use xlink:href="#E1-MJMAIN-22C5" x="15765" y="0"></use>
<g transform="translate(16266,0)">
 <use xlink:href="#E1-MJSZ3-28" x="0" y="-1"></use>
<g transform="translate(736,0)">
<g transform="translate(234,0)">
<g transform="translate(425,0)">
 <use xlink:href="#E1-MJMATHI-72" x="0" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMATHI-74" x="638" y="-213"></use>
</g>
<g transform="translate(0,-673)">
 <use xlink:href="#E1-MJSZ4-E152" x="23" y="0"></use>
<g transform="translate(390,0)">
 <use xlink:href="#E1-MJSZ4-E151"></use>
 <use xlink:href="#E1-MJSZ4-E150" x="450" y="0"></use>
</g>
 <use xlink:href="#E1-MJSZ4-E153" x="1207" y="0"></use>
</g>
</g>
<g transform="translate(0,-1546)">
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-72"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-65" x="392" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-77" x="837" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-61" x="1559" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-72" x="2060" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-64" x="2452" y="0"></use>
</g>
 <use xlink:href="#E1-MJMAIN-2B" x="2349" y="0"></use>
<g transform="translate(3350,0)">
<g transform="translate(1500,0)">
 <use xlink:href="#E1-MJMATHI-3B3" x="557" y="0"></use>
<g transform="translate(-17,-731)">
 <use xlink:href="#E1-MJSZ4-E152" x="23" y="0"></use>
<g transform="translate(390,0)">
 <use xlink:href="#E1-MJSZ4-E151"></use>
 <use xlink:href="#E1-MJSZ4-E150" x="450" y="0"></use>
</g>
 <use xlink:href="#E1-MJSZ4-E153" x="1207" y="0"></use>
</g>
</g>
<g transform="translate(0,-1611)">
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-64"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-69" x="556" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-73" x="835" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-63" x="1229" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-6F" x="1674" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-75" x="2174" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-6E" x="2731" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-74" x="3287" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-66" x="4030" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-61" x="4337" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-63" x="4837" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-74" x="5282" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-6F" x="5671" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-72" x="6172" y="0"></use>
</g>
</g>
 <use xlink:href="#E1-MJMAIN-22C5" x="8214" y="0"></use>
<g transform="translate(8715,0)">
<g transform="translate(1864,0)">
 <use xlink:href="#E1-MJMAIN-6D"></use>
 <use xlink:href="#E1-MJMAIN-61" x="833" y="0"></use>
 <use xlink:href="#E1-MJMAIN-78" x="1334" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMATHI-61" x="1052" y="-866"></use>
 <use xlink:href="#E1-MJMATHI-51" x="2029" y="0"></use>
 <use xlink:href="#E1-MJMAIN-28" x="2820" y="0"></use>
<g transform="translate(3210,0)">
 <use xlink:href="#E1-MJMATHI-73" x="0" y="0"></use>
<g transform="translate(469,-150)">
 <use transform="scale(0.707)" xlink:href="#E1-MJMATHI-74" x="0" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-2B" x="361" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-31" x="1140" y="0"></use>
</g>
</g>
 <use xlink:href="#E1-MJMAIN-2C" x="4939" y="0"></use>
 <use xlink:href="#E1-MJMATHI-61" x="5384" y="0"></use>
 <use xlink:href="#E1-MJMAIN-29" x="5914" y="0"></use>
<g transform="translate(12,-1234)">
 <use xlink:href="#E1-MJSZ4-E152" x="23" y="0"></use>
<g transform="translate(534.1559512794806,0) scale(5.279573818892697,1)">
 <use xlink:href="#E1-MJSZ4-E154"></use>
</g>
<g transform="translate(2701,0)">
 <use xlink:href="#E1-MJSZ4-E151"></use>
 <use xlink:href="#E1-MJSZ4-E150" x="450" y="0"></use>
</g>
<g transform="translate(3652.5769552144134,0) scale(5.279573818892697,1)">
 <use xlink:href="#E1-MJSZ4-E154"></use>
</g>
 <use xlink:href="#E1-MJSZ4-E153" x="5829" y="0"></use>
</g>
</g>
<g transform="translate(0,-2114)">
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-65"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-73" x="444" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-74" x="839" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-69" x="1228" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-6D" x="1507" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-61" x="2340" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-74" x="2841" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-65" x="3230" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-6F" x="4028" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-66" x="4529" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-6F" x="5189" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-70" x="5689" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-74" x="6246" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-69" x="6635" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-6D" x="6914" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-61" x="7747" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-6C" x="8248" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-66" x="8880" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-75" x="9186" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-74" x="9743" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-75" x="10132" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-72" x="10689" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-65" x="11081" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-76" x="11879" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-61" x="12408" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-6C" x="12908" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-75" x="13187" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-65" x="13743" y="0"></use>
</g>
</g>
<g transform="translate(12,-2866)">
 <use xlink:href="#E1-MJSZ4-E152" x="23" y="0"></use>
<g transform="translate(674.8934007451253,0) scale(20.094042183697404,1)">
 <use xlink:href="#E1-MJSZ4-E154"></use>
</g>
<g transform="translate(8923,0)">
 <use xlink:href="#E1-MJSZ4-E151"></use>
 <use xlink:href="#E1-MJSZ4-E150" x="450" y="0"></use>
</g>
<g transform="translate(10015.391117898036,0) scale(20.094042183697404,1)">
 <use xlink:href="#E1-MJSZ4-E154"></use>
</g>
 <use xlink:href="#E1-MJSZ4-E153" x="18273" y="0"></use>
</g>
<g transform="translate(3394,-3778)">
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-6E"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-65" x="556" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-77" x="1001" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-76" x="2077" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-61" x="2605" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-6C" x="3106" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-75" x="3384" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-65" x="3941" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-28" x="4739" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-74" x="5128" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-65" x="5518" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-6D" x="5962" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-70" x="6796" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-6F" x="7352" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-72" x="7853" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-61" x="8245" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-6C" x="8746" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-64" x="9378" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-69" x="9934" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-66" x="10213" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-66" x="10519" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-65" x="10826" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-72" x="11270" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-65" x="11663" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-6E" x="12107" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-63" x="12664" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-65" x="13108" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-74" x="13906" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-61" x="14296" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-72" x="14796" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-67" x="15189" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-65" x="15689" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-74" x="16134" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-29" x="16523" y="0"></use>
</g>
</g>
 <use xlink:href="#E1-MJMAIN-2212" x="19706" y="0"></use>
<g transform="translate(20707,0)">
 <use xlink:href="#E1-MJMATHI-51" x="0" y="0"></use>
 <use xlink:href="#E1-MJMAIN-28" x="791" y="0"></use>
<g transform="translate(1181,0)">
 <use xlink:href="#E1-MJMATHI-73" x="0" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMATHI-74" x="663" y="-213"></use>
</g>
 <use xlink:href="#E1-MJMAIN-2C" x="2006" y="0"></use>
<g transform="translate(2451,0)">
 <use xlink:href="#E1-MJMATHI-61" x="0" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMATHI-74" x="748" y="-213"></use>
</g>
 <use xlink:href="#E1-MJMAIN-29" x="3336" y="0"></use>
<g transform="translate(11,-765)">
 <use xlink:href="#E1-MJSZ4-E152" x="23" y="0"></use>
<g transform="translate(505.0007098332299,0) scale(2.2106010350768335,1)">
 <use xlink:href="#E1-MJSZ4-E154"></use>
</g>
<g transform="translate(1412,0)">
 <use xlink:href="#E1-MJSZ4-E151"></use>
 <use xlink:href="#E1-MJSZ4-E150" x="450" y="0"></use>
</g>
<g transform="translate(2334.4531445655,0) scale(2.2106010350768335,1)">
 <use xlink:href="#E1-MJSZ4-E154"></use>
</g>
 <use xlink:href="#E1-MJSZ4-E153" x="3251" y="0"></use>
</g>
<g transform="translate(449,-1638)">
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-6F"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-6C" x="500" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-64" x="779" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-76" x="1689" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-61" x="2217" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-6C" x="2718" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-75" x="2996" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-65" x="3553" y="0"></use>
</g>
</g>
 <use xlink:href="#E1-MJSZ3-29" x="24433" y="-1"></use>
<g transform="translate(12,1772)">
 <use xlink:href="#E1-MJSZ4-E150" x="23" y="0"></use>
<g transform="translate(747.5214584619531,0) scale(27.73910089073191,1)">
 <use xlink:href="#E1-MJSZ4-E154"></use>
</g>
<g transform="translate(12134,0)">
 <use xlink:href="#E1-MJSZ4-E153"></use>
 <use xlink:href="#E1-MJSZ4-E152" x="450" y="0"></use>
</g>
<g transform="translate(13298.943832569355,0) scale(27.73910089073191,1)">
 <use xlink:href="#E1-MJSZ4-E154"></use>
</g>
 <use xlink:href="#E1-MJSZ4-E151" x="24695" y="0"></use>
</g>
<g transform="translate(9606,2355)">
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-74"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-65" x="389" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-6D" x="833" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-70" x="1667" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-6F" x="2224" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-72" x="2724" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-61" x="3117" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-6C" x="3617" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-64" x="4249" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-69" x="4806" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-66" x="5084" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-66" x="5391" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-65" x="5697" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-72" x="6142" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-65" x="6534" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-6E" x="6979" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-63" x="7535" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-65" x="7980" y="0"></use>
</g>
</g>
</g>
</svg>

source: https://en.wikipedia.org/wiki/Q-learning





In program we used min-max algorithm via internet to test our algorithm.

